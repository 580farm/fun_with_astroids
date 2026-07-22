from __future__ import annotations

import sys

try:
    import pygame
except ImportError as exc:  # pragma: no cover - depends on local environment
    raise SystemExit(
        "pygame-ce is required. Install it with: python -m pip install -e \".[dev]\""
    ) from exc

from .config import (
    ASTEROID,
    ASTEROID_OUTLINE,
    SETTINGS,
    SHIP,
    SHIP_THRUST,
    SPACE,
    STAR,
    TEXT,
    WARNING,
)
from .entities import Ship, create_asteroid, create_asteroid_wave
from .scoring import calculate_score, credits_from_score


def main() -> None:
    pygame.init()
    pygame.display.set_caption(SETTINGS.title)
    screen = pygame.display.set_mode((SETTINGS.width, SETTINGS.height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    large_font = pygame.font.Font(None, 56)

    ship = Ship(
        position=pygame.Vector2(SETTINGS.ship_x, SETTINGS.height / 2),
    )
    asteroids = create_asteroid_wave(SETTINGS.asteroid_count)

    elapsed = 0.0
    collisions = 0
    asteroids_dodged = 0
    running = True
    round_complete = False

    while running:
        dt = clock.tick(SETTINGS.fps) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        if not round_complete:
            elapsed += dt
            round_complete = elapsed >= SETTINGS.round_seconds

            keys = pygame.key.get_pressed()
            ship.update(dt, keys)
            for asteroid_index, asteroid in enumerate(asteroids):
                asteroid.update(dt)
                if asteroid.is_off_screen:
                    asteroids_dodged += 1
                    farthest_x = max(other.position.x for other in asteroids)
                    asteroids[asteroid_index] = create_asteroid(farthest_x + 170)

            if ship.hit_cooldown == 0:
                for asteroid in asteroids:
                    if ship.collides_with(asteroid):
                        collisions += 1
                        ship.mark_hit()
                        ship.vertical_speed = -180.0
                        break

        seconds_remaining = max(0.0, SETTINGS.round_seconds - elapsed)
        seconds_survived = min(elapsed, SETTINGS.round_seconds)
        score = calculate_score(seconds_survived, collisions, asteroids_dodged)
        credits = credits_from_score(score.total)

        screen.fill(SPACE)
        draw_scroll_lines(screen, pygame.time.get_ticks())
        draw_stars(screen)
        draw_asteroids(screen, asteroids)
        draw_ship(screen, ship, pygame.key.get_pressed())
        draw_hud(
            screen,
            font,
            seconds_remaining,
            score.total,
            collisions,
            asteroids_dodged,
            credits,
        )

        if round_complete:
            draw_round_complete(screen, large_font, font, score.total, credits)

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)


def draw_stars(screen: pygame.Surface) -> None:
    star_points = (
        (80, 70),
        (180, 180),
        (310, 95),
        (500, 145),
        (760, 90),
        (890, 220),
        (110, 520),
        (265, 455),
        (430, 560),
        (610, 405),
        (830, 520),
    )
    for x, y in star_points:
        pygame.draw.circle(screen, STAR, (x, y), 1)


def draw_scroll_lines(screen: pygame.Surface, elapsed_ticks: int) -> None:
    offset = (elapsed_ticks // 18) % 80
    for x in range(-80, SETTINGS.width + 80, 80):
        start_x = x - offset
        pygame.draw.line(
            screen,
            (18, 27, 48),
            (start_x, 0),
            (start_x - 120, SETTINGS.height),
        )


def draw_ship(
    screen: pygame.Surface,
    ship: Ship,
    keys: pygame.key.ScancodeWrapper,
) -> None:
    tilt = max(
        -0.45,
        min(0.45, -ship.vertical_speed / SETTINGS.max_vertical_speed * 0.45),
    )
    nose = pygame.Vector2(24, 0).rotate_rad(tilt)
    left = pygame.Vector2(-18, -14).rotate_rad(tilt)
    right = pygame.Vector2(-18, 14).rotate_rad(tilt)
    points = [
        ship.position + nose,
        ship.position + left,
        ship.position + right,
    ]
    color = WARNING if ship.hit_cooldown > 0 else SHIP
    pygame.draw.polygon(screen, color, points, width=2)

    thrusting_up = keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]
    thrusting_down = keys[pygame.K_DOWN] or keys[pygame.K_s]

    if thrusting_up:
        flame = ship.position - nose.normalize() * 20
        pygame.draw.circle(screen, SHIP_THRUST, flame, 5)
        pygame.draw.circle(screen, SHIP_THRUST, ship.position + pygame.Vector2(-6, 18), 4)
    if thrusting_down:
        pygame.draw.circle(screen, SHIP_THRUST, ship.position + pygame.Vector2(-6, -18), 4)


def draw_asteroids(screen: pygame.Surface, asteroids: list) -> None:
    for asteroid in asteroids:
        pygame.draw.circle(screen, ASTEROID, asteroid.position, asteroid.radius)
        pygame.draw.circle(
            screen,
            ASTEROID_OUTLINE,
            asteroid.position,
            asteroid.radius,
            width=3,
        )


def draw_hud(
    screen: pygame.Surface,
    font: pygame.font.Font,
    seconds_remaining: float,
    score: int,
    collisions: int,
    asteroids_dodged: int,
    credits: int,
) -> None:
    hud = (
        f"Time {int(seconds_remaining):02d}  "
        f"Score {score:04d}  "
        f"Hits {collisions}  "
        f"Dodged {asteroids_dodged}  "
        f"Credits {credits}"
    )
    screen.blit(font.render(hud, True, TEXT), (24, 22))


def draw_round_complete(
    screen: pygame.Surface,
    large_font: pygame.font.Font,
    font: pygame.font.Font,
    score: int,
    credits: int,
) -> None:
    overlay = pygame.Surface((SETTINGS.width, SETTINGS.height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    title = large_font.render("Level Complete", True, TEXT)
    detail = font.render(
        f"Score {score} | Credits earned {credits} | Press Escape to quit",
        True,
        TEXT,
    )
    screen.blit(
        title,
        title.get_rect(center=(SETTINGS.width / 2, SETTINGS.height / 2 - 30)),
    )
    screen.blit(
        detail,
        detail.get_rect(center=(SETTINGS.width / 2, SETTINGS.height / 2 + 25)),
    )

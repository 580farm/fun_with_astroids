from __future__ import annotations

import math
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
from .entities import Ship, create_asteroids
from .scoring import calculate_score, credits_from_score


def main() -> None:
    pygame.init()
    pygame.display.set_caption(SETTINGS.title)
    screen = pygame.display.set_mode((SETTINGS.width, SETTINGS.height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)
    large_font = pygame.font.Font(None, 56)

    ship = Ship(
        position=pygame.Vector2(SETTINGS.width / 2, SETTINGS.height / 2),
        velocity=pygame.Vector2(0, 0),
    )
    asteroids = create_asteroids(SETTINGS.asteroid_count, ship.position)

    elapsed = 0.0
    collisions = 0
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
            for asteroid in asteroids:
                asteroid.update(dt)

            if ship.hit_cooldown == 0:
                for asteroid in asteroids:
                    if ship.collides_with(asteroid):
                        collisions += 1
                        ship.mark_hit()
                        ship.velocity *= -0.35
                        break

        seconds_remaining = max(0.0, SETTINGS.round_seconds - elapsed)
        score = calculate_score(seconds_remaining, collisions)
        credits = credits_from_score(score.total)

        screen.fill(SPACE)
        draw_stars(screen)
        draw_asteroids(screen, asteroids)
        draw_ship(screen, ship, pygame.key.get_pressed())
        draw_hud(screen, font, seconds_remaining, score.total, collisions, credits)

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


def draw_ship(
    screen: pygame.Surface,
    ship: Ship,
    keys: pygame.key.ScancodeWrapper,
) -> None:
    radians = math.radians(ship.angle)
    nose = pygame.Vector2(math.cos(radians), math.sin(radians)) * 22
    left = pygame.Vector2(math.cos(radians + 2.45), math.sin(radians + 2.45)) * 18
    right = pygame.Vector2(math.cos(radians - 2.45), math.sin(radians - 2.45)) * 18
    points = [
        ship.position + nose,
        ship.position + left,
        ship.position + right,
    ]
    color = WARNING if ship.hit_cooldown > 0 else SHIP
    pygame.draw.polygon(screen, color, points, width=2)

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        flame = ship.position - nose.normalize() * 16
        pygame.draw.circle(screen, SHIP_THRUST, flame, 5)


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
    credits: int,
) -> None:
    hud = (
        f"Time {int(seconds_remaining):02d}  "
        f"Score {score:04d}  "
        f"Hits {collisions}  "
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

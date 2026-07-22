from dataclasses import dataclass
import random

import pygame

from .config import SETTINGS


def clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))


@dataclass
class Ship:
    position: pygame.Vector2
    vertical_speed: float = 0.0
    radius: int = SETTINGS.ship_radius
    hit_cooldown: float = 0.0

    def update(self, dt: float, keys: pygame.key.ScancodeWrapper) -> None:
        thrusting_up = keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]
        thrusting_down = keys[pygame.K_DOWN] or keys[pygame.K_s]

        if thrusting_up:
            self.vertical_speed -= SETTINGS.vertical_thrust * dt
        if thrusting_down:
            self.vertical_speed += SETTINGS.vertical_thrust * dt

        if not thrusting_up and not thrusting_down:
            self.vertical_speed *= SETTINGS.vertical_damping ** (dt * SETTINGS.fps)
            if abs(self.vertical_speed) < 2.0:
                self.vertical_speed = 0.0

        self.vertical_speed = clamp(
            self.vertical_speed,
            -SETTINGS.max_vertical_speed,
            SETTINGS.max_vertical_speed,
        )
        self.position.y += self.vertical_speed * dt
        self.position.x = SETTINGS.ship_x

        top = self.radius
        bottom = SETTINGS.height - self.radius
        clamped_y = clamp(self.position.y, top, bottom)
        if clamped_y != self.position.y:
            self.vertical_speed = 0.0
        self.position.y = clamped_y
        self.hit_cooldown = max(0.0, self.hit_cooldown - dt)

    def collides_with(self, asteroid: "Asteroid") -> bool:
        distance = self.position.distance_to(asteroid.position)
        return distance <= self.radius + asteroid.radius

    def mark_hit(self) -> None:
        self.hit_cooldown = 1.0


@dataclass
class Asteroid:
    position: pygame.Vector2
    radius: int
    speed: float = SETTINGS.asteroid_speed

    def update(self, dt: float) -> None:
        self.position.x -= self.speed * dt

    @property
    def is_off_screen(self) -> bool:
        return self.position.x < -self.radius


def create_asteroid(x: float | None = None) -> Asteroid:
    radius = random.choice((18, 24, 32, 40))
    y = random.randrange(radius + 16, SETTINGS.height - radius - 16)
    start_x = x if x is not None else SETTINGS.width + random.randrange(40, 260)
    speed = SETTINGS.asteroid_speed + random.uniform(-35, 55)
    return Asteroid(position=pygame.Vector2(start_x, y), radius=radius, speed=speed)


def create_asteroid_wave(count: int) -> list[Asteroid]:
    spacing = SETTINGS.width / max(1, count)
    return [
        create_asteroid(SETTINGS.width + 160 + spacing * index)
        for index in range(count)
    ]

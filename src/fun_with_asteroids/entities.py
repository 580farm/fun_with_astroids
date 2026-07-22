from dataclasses import dataclass
import math
import random

import pygame

from .config import SETTINGS


def wrap_position(position: pygame.Vector2, width: int, height: int) -> pygame.Vector2:
    return pygame.Vector2(position.x % width, position.y % height)


@dataclass
class Ship:
    position: pygame.Vector2
    velocity: pygame.Vector2
    angle: float = -90.0
    radius: int = SETTINGS.ship_radius
    hit_cooldown: float = 0.0

    def update(self, dt: float, keys: pygame.key.ScancodeWrapper) -> None:
        turn_speed = 210.0
        thrust = 310.0
        drag = 0.992

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= turn_speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += turn_speed * dt
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            radians = math.radians(self.angle)
            direction = pygame.Vector2(math.cos(radians), math.sin(radians))
            self.velocity += direction * thrust * dt

        self.velocity *= drag
        self.position += self.velocity * dt
        self.position = wrap_position(self.position, SETTINGS.width, SETTINGS.height)
        self.hit_cooldown = max(0.0, self.hit_cooldown - dt)

    def collides_with(self, asteroid: "Asteroid") -> bool:
        distance = self.position.distance_to(asteroid.position)
        return distance <= self.radius + asteroid.radius

    def mark_hit(self) -> None:
        self.hit_cooldown = 1.0


@dataclass
class Asteroid:
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: int

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.position = wrap_position(self.position, SETTINGS.width, SETTINGS.height)


def create_asteroids(count: int, ship_position: pygame.Vector2) -> list[Asteroid]:
    asteroids: list[Asteroid] = []

    while len(asteroids) < count:
        position = pygame.Vector2(
            random.randrange(0, SETTINGS.width),
            random.randrange(0, SETTINGS.height),
        )
        if position.distance_to(ship_position) < 140:
            continue

        speed = random.uniform(45, 145)
        angle = random.uniform(0, math.tau)
        velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
        radius = random.choice((18, 24, 32, 40))
        asteroids.append(Asteroid(position=position, velocity=velocity, radius=radius))

    return asteroids

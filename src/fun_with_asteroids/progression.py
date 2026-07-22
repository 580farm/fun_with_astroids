from dataclasses import dataclass


@dataclass(frozen=True)
class Spacecraft:
    name: str
    program: str
    era: str
    handling: str


@dataclass(frozen=True)
class Upgrade:
    name: str
    tree: str
    cost: int
    description: str
    requires: tuple[str, ...] = ()


STARTER_SPACECRAFT = (
    Spacecraft(
        name="Mercury",
        program="United States",
        era="1960s",
        handling="Small capsule with beginner-friendly handling.",
    ),
    Spacecraft(
        name="Vostok",
        program="Soviet Union",
        era="1960s",
        handling="Stable capsule with forgiving drift.",
    ),
    Spacecraft(
        name="Gemini",
        program="United States",
        era="1960s",
        handling="Training-focused capsule with stronger maneuvering.",
    ),
)


STARTER_UPGRADES = (
    Upgrade(
        name="Faster Turning",
        tree="Pilot",
        cost=3,
        description="Increase ship rotation speed.",
    ),
    Upgrade(
        name="Shield",
        tree="Engineer",
        cost=5,
        description="Absorb one asteroid collision.",
    ),
    Upgrade(
        name="Radar",
        tree="Navigator",
        cost=4,
        description="Warn when asteroids are nearby.",
    ),
)

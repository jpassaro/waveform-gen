import math

from .cli import make_command


@make_command
def sine(x):
    """Regular sine wave. implemented as a sanity check."""
    return math.cos(x * math.pi / 2)


@make_command
def circle(x):
    """Semicircles arranged as a wave."""
    return math.sqrt(1.0 - x ** 2)


@make_command
def parabola(x):
    """Truncated parabolas, arranged as a wave."""
    return 1.0 - x ** 2


@make_command
def square(x):
    """Regular square wave: 1, -1, 1, -1..."""
    return 1


@make_command
def quartic(x):
    """Truncated quartic curve, arranged as a wave"""
    return 1 - x ** 4


@make_command
def unquartic(x):
    """The curve y^4 + x^4 = 1, arranged as a wave. Compare
    "circle"."""
    return (1 - x ** 4) ** (1. / 4)

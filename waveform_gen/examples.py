import math

from .cli import make_command


@make_command
def sine(x):
    return math.cos(x * math.pi / 2)


@make_command
def circle(x):
    return math.sqrt(1.0 - x ** 2)


@make_command
def parabola(x):
    return 1.0 - x ** 2


@make_command
def square(x):
    return 1


@make_command
def quartic(x):
    return 1 - x ** 4


@make_command
def unquartic(x):
    return (1 - x ** 4) ** (1. / 4)

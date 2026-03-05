import numpy as np


def linear(x, a=1, b=0):
    """Lineární funkce: f(x) = ax + b"""
    return a * x + b


def quadratic(x, a=1, b=0, c=0):
    """Kvadratická funkce: f(x) = ax^2 + bx + c"""
    return a * x**2 + b * x + c


def sine(x, amplitude=1, frequency=1, phase=0):
    """Sinusová funkce: f(x) = amplitude * sin(frequency * x + phase)"""
    return amplitude * np.sin(frequency * x + phase)


def cosine(x, amplitude=1, frequency=1, phase=0):
    """Kosinusová funkce: f(x) = amplitude * cos(frequency * x + phase)"""
    return amplitude * np.cos(frequency * x + phase)


def exponential(x, base=np.e, scale=1):
    """Exponenciální funkce: f(x) = scale * base^x"""
    return scale * np.power(base, x)


def logarithm(x, base=np.e):
    """Logaritmická funkce: f(x) = log_base(x), pouze pro x > 0"""
    x_positive = np.where(x > 0, x, np.nan)
    return np.log(x_positive) / np.log(base)


FUNCTIONS = {
    "linear": linear,
    "quadratic": quadratic,
    "sin": sine,
    "cos": cosine,
    "exp": exponential,
    "log": logarithm,
}
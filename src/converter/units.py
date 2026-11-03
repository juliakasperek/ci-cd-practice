"""Simple unit conversions. Small on purpose: the point of this repo is CI/CD."""


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    if km < 0:
        raise ValueError("distance can't be negative")
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    if miles < 0:
        raise ValueError("distance can't be negative")
    return miles / 0.621371


def kg_to_lb(kg: float) -> float:
    if kg < 0:
        raise ValueError("weight can't be negative")
    return kg * 2.20462


def lb_to_kg(lb: float) -> float:
    if lb < 0:
        raise ValueError("weight can't be negative")
    return lb * 2.20462262

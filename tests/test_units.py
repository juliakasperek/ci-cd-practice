import pytest

from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_lb,
    km_to_miles,
    miles_to_km,
)


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 213


def test_fahrenheit_round_trip():
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(37)) == pytest.approx(37)


def test_marathon_in_miles():
    assert km_to_miles(42.195) == pytest.approx(26.219, abs=0.001)


def test_miles_round_trip():
    assert miles_to_km(km_to_miles(10)) == pytest.approx(10)


def test_negative_distance_rejected():
    with pytest.raises(ValueError):
        km_to_miles(-1)


def test_kg_to_lb():
    assert kg_to_lb(1) == pytest.approx(2.20462)


def test_negative_weight_rejected():
    with pytest.raises(ValueError):
        kg_to_lb(-5)


# EXERCISE (Level 1): add tests for lb_to_kg here.

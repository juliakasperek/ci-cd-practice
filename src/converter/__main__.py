"""Command line: python -m converter 100 c f"""

import sys

from . import units

CONVERSIONS = {
    ("c", "f"): units.celsius_to_fahrenheit,
    ("f", "c"): units.fahrenheit_to_celsius,
    ("km", "mi"): units.km_to_miles,
    ("mi", "km"): units.miles_to_km,
    ("kg", "lb"): units.kg_to_lb,
    ("lb", "kg"): units.lb_to_kg,
}


def main(argv: list) -> int:
    if len(argv) != 3:
        print("usage: python -m converter <value> <from> <to>   e.g. 100 c f")
        return 1
    value, src, dst = argv
    func = CONVERSIONS.get((src.lower(), dst.lower()))
    if func is None:
        print(f"don't know how to convert {src} to {dst}")
        return 1
    print(f"{value} {src} = {func(float(value)):.2f} {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

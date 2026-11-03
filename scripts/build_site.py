"""Builds a small static web page (site/index.html) from the converter.

This gives the project something real to deploy in Level 4 (CD).
Run it with:  python scripts/build_site.py
"""

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from converter import celsius_to_fahrenheit, kg_to_lb, km_to_miles  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "site"


def rows(values, func, a, b):
    return "\n".join(f"<tr><td>{v} {a}</td><td>{func(v):.1f} {b}</td></tr>" for v in values)


def main() -> None:
    built = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Converter</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 40rem; margin: 2rem auto;
         padding: 0 1rem; }}
  table {{ border-collapse: collapse; margin-bottom: 2rem; }}
  td {{ border: 1px solid #ccc; padding: .4rem .8rem; }}
  footer {{ color: #666; font-size: .9rem; }}
</style>
</head>
<body>
<h1>Unit converter</h1>
<h2>Temperature</h2>
<table>{rows([-10, 0, 20, 37, 100], celsius_to_fahrenheit, "°C", "°F")}</table>
<h2>Distance</h2>
<table>{rows([1, 5, 10, 21.1, 42.2], km_to_miles, "km", "mi")}</table>
<h2>Weight</h2>
<table>{rows([10, 0, 20, 37, 100], kg_to_lb, "kg", "lb")}</table>
<footer>Deployed automatically by GitHub Actions · built {built}</footer>
</body>
</html>
"""
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {OUT / 'index.html'}")


if __name__ == "__main__":
    main()

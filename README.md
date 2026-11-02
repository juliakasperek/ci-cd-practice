# CI/CD Practice

A tiny Python unit converter used to learn **CI/CD with GitHub Actions**.
The app is small on purpose, so the focus stays on the pipeline around it.

## Run it locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

pytest                              # run the tests
ruff check .                        # run the linter
PYTHONPATH=src python -m converter 100 c f
python scripts/build_site.py        # builds site/index.html
```

## The levels

Work through these in order. Each level has hints in [HINTS.md](HINTS.md),
which start vague and get more specific. Try them on your own first.

### Level 1: Your first CI pipeline
- [ ] Create `.github/workflows/ci.yml` that runs `pytest` on every push.
- [ ] Push it and find the run in the **Actions** tab. It should be green ✅.
- [ ] Break a test on purpose (e.g. change `212` to `213`), push, and watch it go red ❌. Read the log to find *which* test failed.
- [ ] Fix it, then implement `lb_to_kg` in `src/converter/units.py` and add tests for it.

### Level 2: Code quality checks
- [ ] Add a step to your workflow that runs `ruff check .`
- [ ] Push some messy code (an unused import works) and watch the linter fail the build.
- [ ] Run the tests on Python 3.9, 3.11 and 3.13 at once using a **matrix**.

### Level 3: Pull requests and branch protection
- [ ] Make a branch (`git switch -c add-temperature-kelvin`), add a Kelvin conversion with tests, push it, and open a pull request.
- [ ] Notice the checks run on the pull request itself.
- [ ] Turn on branch protection for `main` so pull requests can't merge unless the checks pass.
- [ ] Open a pull request with a failing test and confirm GitHub blocks the merge.

### Level 4: Continuous deployment
- [ ] Add a second job that runs `python scripts/build_site.py` and deploys `site/` to GitHub Pages.
- [ ] Make it run **only** on `main`, and **only if** the tests passed.
- [ ] Change something, merge it, and watch your live page update by itself.

### Level 5: Extras
- [ ] Add a status badge for your workflow to the top of this README.
- [ ] Cache pip downloads to make runs faster.
- [ ] Run the workflow on a schedule (e.g. every Monday).
- [ ] Create a GitHub Release automatically when you push a version tag like `v1.0.0`.

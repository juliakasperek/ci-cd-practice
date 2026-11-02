# Hints

Click a hint to open it. Try the first one before opening the next.

## Level 1: Your first CI pipeline

<details><summary>Hint 1</summary>

Workflows are YAML files in `.github/workflows/`. Each one needs three things:
**when** to run (`on:`), **where** to run (`runs-on:`), and **what** to run (`steps:`).
</details>

<details><summary>Hint 2</summary>

The runner is a fresh, empty computer. Your steps need to:
1. get your code onto it,
2. install Python,
3. install your dependencies,
4. run the tests.

GitHub publishes ready-made actions for steps 1 and 2: `actions/checkout` and `actions/setup-python`.
</details>

<details><summary>Hint 3: skeleton</summary>

```yaml
name: CI
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      # ??? install requirements-dev.txt
      # ??? run the tests
```
</details>

## Level 2: Code quality checks

<details><summary>Hint 1</summary>

A linter is just another command, so it's just another step, like the tests.
</details>

<details><summary>Hint 2: matrix</summary>

Under the job, add:

```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.11", "3.13"]
```

Then use `${{ matrix.python-version }}` where you set the Python version.
GitHub runs one copy of the job per version, in parallel.
</details>

## Level 3: Pull requests and branch protection

<details><summary>Hint 1</summary>

Make the workflow run on pull requests too, not only pushes. Look at what `on:` accepts.
</details>

<details><summary>Hint 2</summary>

Branch protection lives in the repo's **Settings → Branches** (or **Rules → Rulesets**).
Look for "Require status checks to pass". The check only appears in the list after it has run at least once.
</details>

## Level 4: Continuous deployment

<details><summary>Hint 1</summary>

A workflow can have several jobs. `needs: test` makes one job wait for another, and it's
skipped if that one fails. That's the "only deploy if tests pass" part.
</details>

<details><summary>Hint 2</summary>

To limit a job to `main`, add an `if:` condition that checks `github.ref`.
In **Settings → Pages**, set the source to **GitHub Actions**.
</details>

<details><summary>Hint 3: the deploy actions</summary>

GitHub Pages deploys use these actions:
- `actions/upload-pages-artifact` (give it `path: site`)
- `actions/deploy-pages`

The deploy job also needs `permissions:` for `pages: write` and `id-token: write`.
Your portfolio repo has a working example in `.github/workflows/deploy.yml`. Compare them!
</details>

## Level 5: Extras

<details><summary>Hints</summary>

- Badge: on your workflow's page in the Actions tab, open the **⋯** menu and choose **Create status badge**.
- Cache: `actions/setup-python` has a `cache: pip` option.
- Schedule: `on: schedule:` with a `cron:` line. crontab.guru helps you write cron syntax.
- Releases: trigger on `push: tags: ["v*"]` and look at the `gh release create` command.
</details>

# github-actions-test

A small Python project (a discount calculator) with automated tests, a Docker image and GitHub Actions workflows that lint, test, build and push the image to Docker Hub.

## What this demonstrates
- CI with GitHub Actions: linting (flake8) and testing (pytest) on every push and pull request
- A multi-job workflow where the Docker job runs only after tests pass and only on pushes to `master`
- Building a Docker image and pushing it to Docker Hub from CI, with credentials kept in GitHub Secrets
- Containerizing a Python application with a slim base image

## Repository structure
```
github-actions-test/
├── .github/workflows/
│   ├── docker_push.yaml   # Test, build and push Docker image
│   └── python-app.yaml    # Lint and test
├── src/
│   └── app.py             # Discount calculator
├── tests/                 # pytest tests
├── Dockerfile             # Container image for the app
└── requirements.txt       # Python dependencies (pytest)
```

## The app
`src/app.py` is a small discount calculator.

- `calculate_discount(price, discount_percent)` returns the price after the discount, rounded to 2 decimals. It raises a `ValueError` if the price is negative or the discount is below 0 or above 100.
- `main()` applies discounts to three sample products and prints each final price and the total.

Example output:
```
Laptop: ₹72000.0
Keyboard: ₹2550.0
Mouse: ₹1425.0

Total : ₹75975.0
```

## Run it locally
Requires Python 3.10+.

```bash
pip install -r requirements.txt
pytest
python -m src.app
```

## Docker
The image is based on `python:3.10-slim`. It installs the dependencies from `requirements.txt`, copies the `src/` folder and starts the app with `python -m src.app`.

```bash
docker build -t github-actions-test .
docker run --rm github-actions-test
```

## CI/CD workflows

Both workflows run on pushes and pull requests to `master`, using Python 3.10 on `ubuntu-latest`.

### `docker_push.yaml` — Test, Build and Push Docker Image
| Job | Steps |
|---|---|
| **test** | Check out the code, set up Python, install `flake8`, `pytest` and `requirements.txt`, lint with flake8, run `pytest` |
| **docker** | Runs only if `test` passes **and** the event is a push (pull requests run the tests but do not push an image). Logs in to Docker Hub, builds the image and pushes it with the `latest` tag |

The flake8 step runs twice: the first run fails the build on syntax errors and undefined names, and the second reports style and complexity issues as warnings only.

### `python-app.yaml` — Testing GitHub Actions
Installs dependencies, lints with flake8 and runs `pytest`.

### Required repository secrets
The Docker job needs these secrets (Settings → Secrets and variables → Actions):

| Secret | Purpose |
|---|---|
| `DOCKERHUB_USERNAME` | Docker Hub account name |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `DOCKERHUB_REPO` | Name of the Docker Hub repository to push to |


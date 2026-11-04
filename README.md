# Gym Progress API

A REST API for logging workouts, exercises, sets, weights, and RPE, built to track strength training progress over time, with JWT-authenticated user accounts.

## Why I built this

I wanted a backend that models a real use case end-to-end: user auth, relational data (workouts → exercises → sets), and a query pattern that actually matters to lifters (progress over time). It's also my reference implementation for JWT auth and testing FastAPI apps properly, not just wiring up CRUD.

## What it demonstrates

- **Authentication**: JWT-based auth flow — register, login, protected routes via token
- **Relational data modeling**: workouts containing exercises and sets, with SQLAlchemy ORM relationships
- **Testing**: full pytest suite running against an isolated in-memory SQLite database (no shared state between test runs)
- **API design**: RESTful resource structure with FastAPI's automatic OpenAPI/Swagger docs

## Tech stack

FastAPI, SQLAlchemy, SQLite, Pydantic, JWT (`python-jose`), password hashing (`passlib` + bcrypt), pytest.

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Create account |
| POST | `/users/login` | Authenticate & get token |
| GET | `/users/me` | Fetch current user profile |
| POST | `/workouts/` | Log a new workout with exercises/sets |
| GET | `/workouts/` | Get all workouts for logged-in user |
| GET | `/workouts/{id}` | Get specific workout details |

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The app signs JWTs with a secret key that is read from the environment and is never stored in the repo. Create a `.env` file from the template and set a real value:

```bash
cp .env.example .env            # Windows PowerShell: Copy-Item .env.example .env
python -c "import secrets; print(secrets.token_hex(32))"   # paste the output as SECRET_KEY in .env
```

The app will refuse to start if `SECRET_KEY` is missing.

## Running

```bash
python -m uvicorn app.main:app --reload
```

Interactive API docs available at `http://127.0.0.1:8000/docs`.

## Running Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

Tests set their own throwaway `SECRET_KEY` and run against an isolated in-memory SQLite database — no setup required, no side effects on real data.

gym-progress-api
A REST API built with FastAPI and SQLAlchemy for logging workouts, exercises, sets, weights, and RPE. Handles auth using JWT tokens.

Setup
Create and activate a virtual environment:

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
Install dependencies:

PowerShell
pip install -r requirements.txt
Run the dev server:

PowerShell
python -m uvicorn app.main:app --reload
Docs are available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

Running Tests
Tests run against an in-memory SQLite database:

PowerShell
python -m pytest
Endpoints
POST /users/register – Create account

POST /users/login – Authenticate & get token

GET /users/me – Fetch current user profile

POST /workouts/ – Log a new workout with exercises/sets

GET /workouts/ – Get all workouts for logged-in user

GET /workouts/{id} – Get specific workout details

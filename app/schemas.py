from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# --- SET SCHEMAS ---
class SetBase(BaseModel):
    reps: int
    weight: float
    rpe: Optional[float] = None

class SetCreate(SetBase):
    pass

class SetResponse(SetBase):
    id: int
    exercise_id: int

    class Config:
        from_attributes = True


# --- EXERCISE SCHEMAS ---
class ExerciseBase(BaseModel):
    name: str

class ExerciseCreate(ExerciseBase):
    sets: List[SetCreate] = []

class ExerciseResponse(ExerciseBase):
    id: int
    workout_id: int
    sets: List[SetResponse] = []

    class Config:
        from_attributes = True


# --- WORKOUT SCHEMAS ---
class WorkoutBase(BaseModel):
    title: str

class WorkoutCreate(WorkoutBase):
    exercises: List[ExerciseCreate] = []

class WorkoutResponse(WorkoutBase):
    id: int
    date: datetime
    user_id: int
    exercises: List[ExerciseResponse] = []

    class Config:
        from_attributes = True


# --- USER & AUTH SCHEMAS ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
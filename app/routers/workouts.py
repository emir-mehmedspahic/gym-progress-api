from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User, Workout, Exercise, Set
from ..schemas import WorkoutCreate, WorkoutResponse
from .users import get_current_user

router = APIRouter(prefix="/workouts", tags=["Workouts & Logs"])


@router.post("/", response_model=WorkoutResponse, status_code=status.HTTP_201_CREATED)
def create_workout(
    workout_data: WorkoutCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new workout with nested exercises and sets for the authenticated user."""
    
    # 1. Instantiate parent Workout model linked to current user
    new_workout = Workout(
        title=workout_data.title,
        user_id=current_user.id
    )
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)

    # 2. Iterate and append nested exercises & sets
    for ex_data in workout_data.exercises:
        new_exercise = Exercise(
            name=ex_data.name,
            workout_id=new_workout.id
        )
        db.add(new_exercise)
        db.commit()
        db.refresh(new_exercise)

        for set_data in ex_data.sets:
            new_set = Set(
                reps=set_data.reps,
                weight=set_data.weight,
                rpe=set_data.rpe,
                exercise_id=new_exercise.id
            )
            db.add(new_set)

    db.commit()
    db.refresh(new_workout)
    return new_workout


@router.get("/", response_model=List[WorkoutResponse])
def get_my_workouts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve all workout logs belonging exclusively to the authenticated user."""
    workouts = db.query(Workout).filter(Workout.user_id == current_user.id).all()
    return workouts


@router.get("/{workout_id}", response_model=WorkoutResponse)
def get_workout_by_id(
    workout_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve a specific workout log by ID."""
    workout = db.query(Workout).filter(
        Workout.id == workout_id, 
        Workout.user_id == current_user.id
    ).first()

    if not workout:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout log not found.",
        )

    return workout
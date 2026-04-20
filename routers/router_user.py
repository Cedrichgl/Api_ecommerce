from fastapi import APIRouter, Depends, HTTPException
from typing import List
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import get_db
from schemas.schema_user import UserBase, UserCreate, UserResponse, UserUpdate
from models import User

router = APIRouter()

#créer un utilisateur
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # convertir en dict
    data = user.model_dump()
    # retirer password
    password = data.pop("password")
    # hasher
    hashed_password = pwd_context.hash(password[:72])
    # créer user avec le bon champ
    db_user = User(**data, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#obtenir un utilisateur pas son id
@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return db_user


#obtenir tous les utilisateurs
@router.get("/users/", response_model=List[UserResponse])
async def get_all_users(skip:int = 0, limit:int = 0, db:Session = Depends(get_db)):
    db_users = db.query(User).offset(skip).limit(limit).all()
    return db_users



#modification d'un utilisateur
@router.patch("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    for field, value in payload.model_dump(exclude_none=True).items():
        setattr(db_user, field, value)
    db.commit()
    return db_user

@router.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur inexistant")
    db.delete(db_user)
    db.commit()
    return db_user



@router.put("/users/{user_id}", response_model=UserResponse)
async def total_update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Utilisateur inexistant")
    for key, value in payload.model_dump().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user
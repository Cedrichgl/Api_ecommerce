from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.schema_user import UserBase, UserCreate, UserResponse, UserUpdate
from models import Produit

router = APIRouter()



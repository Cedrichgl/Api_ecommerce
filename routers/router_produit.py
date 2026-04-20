from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from schemas.schema_produit import ProduitBase, ProduitCreate, ProduitResponse, ProduitUpdate
from models import Produit

router = APIRouter()


@router.post("/produits/", response_model=ProduitResponse, status_code=201)
async def create_produit(produit: ProduitCreate, db:Session = Depends(get_db)):
    db_produit = Produit(**produit.model_dump())
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit


@router.get("/produits/", response_model=List[ProduitResponse])
async def get_produits(db:Session = Depends(get_db)):
    produits = db.query(Produit).all()
    return produits


@router.get("/produits/{produit_id}", response_model=ProduitResponse)
async def get_produit(produit_id:int, db:Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit introuvable")
    return produit


@router.patch("/produits/{produit_id}", response_model=ProduitUpdate, status_code=200)
async def patch_produit(produit_id:int, payload: ProduitUpdate, db:Session = Depends(get_db)):
    produit = db.query(Produit).filter(Produit.id == produit_id).first()
    if not produit:
        raise HTTPException(status_code=404, detail="Produit introuvable")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(produit, key, value)

    db.add(produit)
    db.commit()
    db.refresh(produit)
    return produit


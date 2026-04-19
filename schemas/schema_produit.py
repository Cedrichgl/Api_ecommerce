from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List


#socle commun de la classe produit
class ProduitBase(BaseModel):
    nom: str
    prix: float
    stock: int
    disponible: bool
    categorie_id: int
    categorie: str

class ProduitCreate(ProduitBase):
    pass

#Mise à jour produit
class ProduitUpdate(ProduitBase):
    nom: Optional[str] = None
    prix: Optional[float] = None
    stock: Optional[int] = None
    disponible: Optional[bool] = None
    categorie_id: Optional[int] = None
    categorie: Optional[str] = None

#Réponse API
class ProduitResponse(ProduitBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
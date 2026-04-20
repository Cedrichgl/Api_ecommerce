from pydantic import BaseModel, ConfigDict
from typing import Optional, List


#le socle commun
class CategoryBase(BaseModel):
    nom: str
    description: str
    produit: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    nom: Optional[str] = None
    description: Optional[str] = None
    produit: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


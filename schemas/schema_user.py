from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import List, Optional


#La classe utilisateur
class UserBase(BaseModel): #socle commun
    nom: str
    email: EmailStr
    numero: int
    rue: str
    code: int
    complement: str

#creation avec Post dans fastAPI, on ajoute le mot de passe, la class UserCreate herite de la classe UserBase
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

#Mise jour des données utilisateurs
class UserUpdate(BaseModel):
    nom: Optional[str] = None
    email: Optional[EmailStr] = None
    numero: Optional[int] = None
    rue: Optional[str] = None
    code: Optional[int] = None
    complement: Optional[str] = None

#La réponse API
class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)



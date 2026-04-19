from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


#class utilisateur
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom: Mapped[str] = mapped_column(String, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    numero: Mapped[int] = mapped_column(Integer, nullable=False)
    rue: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[int] = mapped_column(Integer, nullable=False)
    complement: Mapped[str] = mapped_column(String, nullable=False)


#table categorie
class Categorie(Base):
    __tablename__="categories"
    id : Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    nom : Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    produits = relationship("Produit", back_populates="categorie")


#table produit
class Produit(Base):
    __tablename__="produits"
    id: Mapped[int] = mapped_column(Integer, index=True, primary_key=True)
    nom: Mapped[str] = mapped_column(String, nullable=False)
    prix: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[int] = mapped_column(Boolean, default=True )
    categorie_id = mapped_column(Integer, ForeignKey("categories.id"))
    categorie = relationship("Categorie", back_populates="produits")


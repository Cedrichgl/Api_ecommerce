from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

#l'url
DATABASE_URL = "postgresql://postgres:MotDePasse@localhost:5432/fastapi"

#moteur
engine  = create_engine(DATABASE_URL)

#Session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#classe Base pour tous les moteurs
class Base(DeclarativeBase):
    pass

#fonction qui gère l'accès à la base de données avec les sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



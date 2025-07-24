



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

# Connexion DB
engine = create_engine(DATABASE_URL)

# Session de base (A injecter dans le repo)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


# Injecter la session dns les routes 

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()

# Base pour tous les modeles SQLAlchemy
Base =declarative_base()
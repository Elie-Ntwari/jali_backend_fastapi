
# models/organisation_model.py

from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database import Base # Base héritée de declarative_base()


# Définition du modèle ORM Organisation (correspond à la table "organisations")
class Organisation(Base):
    __tablename__ = "organisations"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    adresse = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telephone = Column(String(30), nullable=False)
    date_creation = Column(TIMESTAMP(timezone=True), server_default=func.now())

    enfants = relationship("Enfant", back_populates="organisation")

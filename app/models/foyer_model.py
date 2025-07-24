from sqlalchemy import Column, Integer, String
from app.database import Base

class Foyer(Base):
    __tablename__ = "maison_accueil"

    id = Column(Integer, primary_key=True, index=True)
    type_foyer = Column(String(50), nullable=False)
    nom_foyer = Column(String(100), nullable=False)
    adresse = Column(String(255), nullable=False)
    contact = Column(String(100), nullable=False)
    age_chef = Column(Integer, nullable=False)
    sexe_chef = Column(Integer, nullable=False)
    niveau_education_mere_recod = Column(Integer, nullable=False)
    etat_logement = Column(String(50), nullable=False)
    nb_pieces_cat = Column(Integer, nullable=False)

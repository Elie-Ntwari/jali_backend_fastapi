# app/models/enfant_model.py

from sqlalchemy import Column, Integer, String, Float, Boolean, SmallInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Enfant(Base):
    __tablename__ = "enfants"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    postnom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    sobriquet = Column(String(100), nullable=True)

    sexe = Column(SmallInteger, nullable=False)  # 1=Homme, 2=Femme
    age_enfant = Column(SmallInteger, nullable=False)
    niveau_scol_regroupe = Column(SmallInteger, nullable=False)

    date_enregistrement = Column(DateTime, default=datetime.utcnow)
    score_initial = Column(Float, nullable=True)
    statut_risque = Column(String(30), nullable=True)

    organisation_id = Column(Integer, ForeignKey("organisations.id"), nullable=False)
    foyer_id = Column(Integer, ForeignKey("maison_accueil.id"), nullable=False)

    # Relations (optionnelles si tu veux pouvoir faire .enfant.foyer ou .organisation)
    organisation = relationship("Organisation", back_populates="enfants")
    foyer = relationship("Foyer", back_populates="enfants")

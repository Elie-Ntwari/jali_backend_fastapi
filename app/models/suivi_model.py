from sqlalchemy import Column, Integer, Float, Boolean, Text, ForeignKey, SmallInteger, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Suivi(Base):
    __tablename__ = "suivis"

    id = Column(Integer, primary_key=True, index=True)
    enfant_id = Column(Integer, ForeignKey("enfants.id"), nullable=False)
    date_suivi = Column(DateTime, default=datetime.utcnow)

    heures_total_travail = Column(Integer, nullable=False)
    scol_actuelle = Column(Boolean, nullable=False)
    difficulte_fonctionnelle = Column(Boolean, nullable=False)
    souffre_punition_physique = Column(Boolean, nullable=False)
    travail_enfant_global = Column(Boolean, nullable=False)
    niveau_scol_regroupe = Column(SmallInteger, nullable=False)
    favorable_correction_physique = Column(Boolean, nullable=False)
    quintile_bien_etre_x = Column(Float, nullable=False)

    score_suivi = Column(Float, nullable=False)
    statut_risque = Column(String(30), nullable=False)
    commentaire_agent = Column(Text, nullable=True)
    conseil_personnalise = Column(Text, nullable=True)

    agent_id = Column(Integer, ForeignKey("agents.id"), nullable=False)

    # Relations (optionnelles)
    enfant = relationship("Enfant", backref="suivis")
    agent = relationship("Agent", backref="suivis")

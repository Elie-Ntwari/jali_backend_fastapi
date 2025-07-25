# app/models/agent_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    mot_de_passe = Column(String(255), nullable=False)
    organisation_id = Column(Integer, ForeignKey("organisations.id"), nullable=False)

    organisation = relationship("Organisation", back_populates="agents")

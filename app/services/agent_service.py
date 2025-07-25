# app/services/agent_service.py
from app.repository.agent_repository import ajouter_agent, get_agent_par_email
from app.models.agent_model import Agent
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.hash import bcrypt

def creer_agent(db: Session, data):
    agent_existant = get_agent_par_email(db, data.email)
    if agent_existant:
        raise HTTPException(status_code=409, detail="Un agent avec cet email existe déjà.")

    hashed_password = bcrypt.hash(data.mot_de_passe)
    nouvel_agent = Agent(
        nom=data.nom,
        email=data.email,
        mot_de_passe=hashed_password,
        organisation_id=data.organisation_id
    )

    agent_ajoute = ajouter_agent(db, nouvel_agent)
    if not agent_ajoute:
        raise HTTPException(status_code=400, detail="Échec lors de la création de l’agent.")

    return agent_ajoute

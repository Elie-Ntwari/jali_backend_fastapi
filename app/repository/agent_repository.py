# app/repository/agent_repository.py
from sqlalchemy.orm import Session
from app.models.agent_model import Agent
from sqlalchemy.exc import IntegrityError

def ajouter_agent(db: Session, agent: Agent):
    try:
        db.add(agent)
        db.commit()
        db.refresh(agent)
        return agent
    except IntegrityError:
        db.rollback()
        return None

def get_agent_par_email(db: Session, email: str):
    return db.query(Agent).filter(Agent.email == email).first()


def get_agent_by_id(db, agent_id: int):
    return db.query(Agent).filter(Agent.id == agent_id).first()

# app/api/agent_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.agent_schema import AgentCreate, AgentOut
from app.services.agent_service import creer_agent
from app.database import get_db

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.post("/create", response_model=AgentOut)
def ajouter_agent(payload: AgentCreate, db: Session = Depends(get_db)):
    agent = creer_agent(db, payload)
    return agent

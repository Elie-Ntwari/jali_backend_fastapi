# app/schemas/agent_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class AgentCreate(BaseModel):
    nom: str
    email: EmailStr
    mot_de_passe: str
    organisation_id: int

class AgentOut(BaseModel):
    id: int
    nom: str
    email: EmailStr
    organisation_id: int

    class Config:
        from_attributes = True

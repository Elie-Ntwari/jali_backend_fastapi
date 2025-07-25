
from fastapi import FastAPI

from app.controllers import agent_controller, enfant_controller, foyer_controller, organisation_controller, suivi_controller


app = FastAPI(title="API JALI - Backend")


# Inclure les roures
app.include_router(organisation_controller.router)
app.include_router(foyer_controller.router)
app.include_router(enfant_controller.router)
app.include_router(agent_controller.router)
app.include_router(suivi_controller.router)
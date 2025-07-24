
from fastapi import FastAPI

from app.controllers import foyer_controller, organisation_controller


app = FastAPI(title="API JALI - Backend")


# Inclure les roures
app.include_router(organisation_controller.router)
app.include_router(foyer_controller.router)

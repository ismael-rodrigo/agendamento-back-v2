from fastapi.middleware.cors import CORSMiddleware
from src.core.routes import user_route , auth_route
from src.settings import settings
from src.schedule.routes import public_user_route

from fastapi import FastAPI


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_route.router ,prefix='')
app.include_router(auth_route.router  ,prefix='/auth')

app.include_router(public_user_route.router , prefix='/schedule')
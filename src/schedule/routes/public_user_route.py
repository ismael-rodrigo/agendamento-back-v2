from fastapi import APIRouter, Body , Form
from src.schedule.schemas.public_user_schema import LoginPublicUserRequest ,LoginPublicUserResponse
from src.core.auth.hash_provider import verify_password
from src.utils.token_provider import tokenPublicManager
from src.core.schemas.token_schemas import LoginToken
from src.core.database.database import db




router = APIRouter()


@router.post('/public-user' )# response_model=LoginPublicUserRequest
def login_public_user(credentials:LoginPublicUserRequest):
    print(credentials)
    return {}



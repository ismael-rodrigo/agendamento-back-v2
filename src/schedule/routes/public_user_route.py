from fastapi import APIRouter, Body , Form, HTTPException ,status
from src.schedule.schemas.public_user_schema import LoginPublicUserRequest ,LoginPublicUserResponse
from src.core.auth.hash_provider import verify_password
from src.utils.token_provider import tokenPublicManager
from src.core.schemas.token_schemas import LoginToken
from src.core.database.database import db




router = APIRouter()


@router.post('/login' )# response_model=LoginPublicUserRequest
def login_public_user(credentials:LoginPublicUserRequest):
    public_user = db['public_user'].find_one({'cpf_user':credentials.cpf_user})
    
    if public_user:
        if not db['public_user'].find_one({'cpf_user':credentials.cpf_user , 'birth_date':credentials.birth_date}):
            raise HTTPException(status.HTTP_400_BAD_REQUEST , detail='birth date invalid')
        else:
            return {'user_infos':}
    


    #USER AVAILABLE:
    #GENERATE RAMDOM SECURITY QUESTION

    #RETURN SECURITY QUESTION + INITIAL CREDENTIALS

    #USER NOT AVAILABLE:
    #RETURN 201 AND INITIALIZE USER

    return {}


@router.post('/security-question')
def verify_security_question():
    pass





from fastapi import APIRouter, Depends, HTTPException ,status
from core.auth.auth_utils import user_logged
from core.auth.hash_provider import verify_password
from core.auth.token_provider import create_access_token, refresh_token
from core.schemas.token_schemas import LoginToken, RefreshToken
from core.database.database import db
from core.schemas.user_schema import User
from jose import JWTError


router = APIRouter()


@router.get('/public-user')
def get_token(credentials:LoginToken):

    user = db['users'].find_one({'username':credentials.username})
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST , detail='password or username invalid')

    if not verify_password(credentials.password ,user['password']):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED ,detail='password or username invalid')
    
    token = create_access_token({'sub':str(user['_id'])})
    return token

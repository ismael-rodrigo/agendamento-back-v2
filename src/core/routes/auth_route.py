from fastapi import APIRouter, Depends, HTTPException ,status
from src.core.auth.auth_utils import user_logged
from src.core.auth.hash_provider import verify_password
from src.utils.token_provider import tokenManager
from src.core.schemas.token_schemas import LoginToken, RefreshToken
from src.core.database.database import db
from src.core.schemas.user_schema import User
from jose import JWTError


router = APIRouter()



@router.post('/token')
def get_token(credentials:LoginToken):

    user = db['users'].find_one({'username':credentials.username})
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST , detail='password or username invalid')

    if not verify_password(credentials.password ,user['password']):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED ,detail='password or username invalid')
    
    token = tokenManager.create_token(user , 'username')
    return token



@router.get('/verify' )
def verify(user:User = Depends(user_logged)): 
    return HTTPException(status.HTTP_200_OK ,detail='token is valid')



@router.post('/refresh')
def refresh(refresh :RefreshToken):
    try:
        access = tokenManager.refresh_token(refresh.refresh)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='invalid refresh token')

    return access
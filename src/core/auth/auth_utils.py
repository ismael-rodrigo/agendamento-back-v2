from bson import ObjectId
from fastapi import Depends, HTTPException ,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from src.core.database.database import db
from src.utils.token_provider import tokenManager , tokenPublicManager


oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/token')


def user_logged(token:str = Depends(oauth2_schema)):
    try:
        data = tokenManager.verify_token(token)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')

    user = db['users'].find_one({'_id':ObjectId(data)})
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')    
    return user

def user_public_logged(token:str = Depends(oauth2_schema)):
    try:
        data = tokenPublicManager.verify_token(token)
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')

    user = db['users'].find_one({'_id':ObjectId(data)})
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED , detail='token invalid')    
    return user
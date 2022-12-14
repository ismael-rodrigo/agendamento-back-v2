from typing import Literal
from pydantic import BaseModel


class PublicUser(BaseModel):
    cpf_user:str
    birth_date:str

    fullname:str
    mother_name:str
    phone_number:str
    
    status: Literal[ 'created' , 'infos_seted']

    available_user:bool
    

class LoginPublicUserRequest(BaseModel):
    cpf_user:str
    birth_date:str

class LoginPublicUserResponse(BaseModel):
    user_infos:PublicUser
    token:str


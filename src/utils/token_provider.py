from datetime import datetime, timedelta
from jose import jwt
from src.settings import settings




class TokenManager():
    
    def __init__(self , SECRET_KEY ,REFRESH_SECRET_KEY ,ACCESS_EXPIRES_IN_MIN=10 , REFRESH_EXPIRES_IN_MIN=20 ):
        self._SECRET_KEY = SECRET_KEY
        self._REFRESH_SECRET_KEY = REFRESH_SECRET_KEY
        self._ACCESS_EXPIRES_IN_MIN = ACCESS_EXPIRES_IN_MIN
        self._REFRESH_EXPIRES_IN_MIN = REFRESH_EXPIRES_IN_MIN
        self._ALGORITHM = settings.ALGORITHM

        
    
    def create_token(self,_data:dict , key:str):
        self.key_user_token = key
        _data = {'sub':str(_data[key])}
        
        data_access ,data_refresh = _data.copy() , _data.copy() 

        expiration_access = datetime.utcnow() + timedelta(minutes=self._ACCESS_EXPIRES_IN_MIN)
        expiration_refresh = datetime.utcnow() + timedelta(minutes=self._REFRESH_EXPIRES_IN_MIN)

        data_access.update({'exp':expiration_access})
        data_refresh.update({'exp':expiration_refresh})

        access_token = jwt.encode(data_access ,key=self._SECRET_KEY , algorithm=self._ALGORITHM )
        refresh_token = jwt.encode(data_refresh ,key=self._REFRESH_SECRET_KEY , algorithm=self._ALGORITHM )

        return {
            'access' :access_token,
            'refresh':refresh_token
        }



    def verify_token(self,token:str):
        data = jwt.decode(token ,key=self._SECRET_KEY ,algorithms=[self._ALGORITHM])
        return data.get('sub')[self.key_user_token]




    def refresh_token(self, refresh_token:str  ):

        data = jwt.decode(token=refresh_token ,key=self._REFRESH_SECRET_KEY ,algorithms=[self._ALGORITHM])
        expiration_access = datetime.utcnow() + timedelta(minutes=self._ACCESS_EXPIRES_IN_MIN)
        data.update({'exp':expiration_access})
        new_access_token = jwt.encode(data , self._SECRET_KEY ,algorithm=self._ALGORITHM)

        return {"access": new_access_token}

    def refresh_with_access_token(self , access_token:str):
        data = jwt.decode(token=access_token ,key=self._SECRET_KEY ,algorithms=[self._ALGORITHM])
        expiration_access = datetime.utcnow() + timedelta(minutes=self._ACCESS_EXPIRES_IN_MIN)
        data.update({'exp':expiration_access})
        new_access_token = jwt.encode(data , self._SECRET_KEY ,algorithm=self._ALGORITHM)

        return {"access": new_access_token}
    


tokenManager = TokenManager(
    settings.SECRET_KEY,
    settings.REFRESH_SECRET_KEY,
    settings.ACCESS_EXPIRES_IN_MIN,
    settings.REFRESH_EXPIRES_IN_MIN)



tokenPublicManager = TokenManager(
    settings.SECRET_KEY,
    settings.REFRESH_SECRET_KEY,
    settings.ACCESS_EXPIRES_IN_MIN,
     settings.REFRESH_EXPIRES_IN_MIN)
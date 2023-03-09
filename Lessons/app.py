from datetime import datetime, timedelta

from pydantic import BaseModel, EmailStr, Field, validator
from passlib.context import CryptContext
from fastapi import FastAPI, HTTPException, Header
from sqlalchemy import select
from jose import jwt, JWTError

from models import User


SECRET_KEY = 'ftgyhujipoknovioeipvmnweruimigu3i0w9umg4m9cgmi49r'
ALGORITHM = 'HS256'
EXPIRE_TOKEN = 5


class UserRegisterModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    # @validator('email', pre=True)
    # def validate_email(cls, value):
    #     with User.session() as session:
    #         obj = session.scalars(
    #             select(User)
    #             .filter_by(email=value.lower())
    #         ).all()
    #         print(obj)
    #         if obj:
    #             raise ValueError('email is not unique')
    #         else:
    #             return value.lower()


class UserInDBModel(UserRegisterModel):
    password: str = Field(default=None)
    hashed_password: str


class TokenModel(BaseModel):
    access_token: str
    token_type: str


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_pass_hash(password):
    return pwd_context.hash(password)


def validate_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def create_access_token(email: str):
    data = {
        'user': email,
        'exp': datetime.utcnow() + timedelta(minutes=EXPIRE_TOKEN)
    }
    return jwt.encode(data, SECRET_KEY)


app = FastAPI()


@app.post('/register/', response_model=UserRegisterModel)
async def register_handler(user: UserRegisterModel):
    users = await User.all(email=user.email)

    if users:
        raise HTTPException(422, detail='email is not unique')
    else:
        hash_pass = get_pass_hash(user.password)
        user_ = User(email=user.email, hashed_password=hash_pass)
        await user_.save()
        return user


@app.post('/login/', response_model=TokenModel)
async def login_handler(user: UserRegisterModel):
    user_in_db = await User.all(email=user.email)
    if user:
        user_in_db = user_in_db[0]
        if validate_password(user.password, user_in_db.hashed_password):
            return {'access_token': create_access_token(user.email), 'token_type': 'Bearer'}
        raise HTTPException(401, detail='email or password is invalid')


@app.get('/profile/')
async def profile_handler(authorization=Header()):
    if authorization.startswith('Bearer'):
        try:
            data = jwt.decode(authorization.removeprefix('Bearer '), SECRET_KEY, [ALGORITHM])
        except JWTError:
            raise HTTPException(401, 'invalid token or token type')
        else:
            return data
    raise HTTPException(401, 'invalid token or token type')
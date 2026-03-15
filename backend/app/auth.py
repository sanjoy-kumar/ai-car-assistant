from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password):

    return pwd_context.hash(password)


def verify_password(password, hashed):

    return pwd_context.verify(password, hashed)


def create_access_token(data):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=24)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

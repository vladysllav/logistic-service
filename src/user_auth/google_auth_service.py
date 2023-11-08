from datetime import datetime, timedelta

import jwt
from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework.exceptions import AuthenticationFailed

from config.settings import GOOGLE_CLIENT_ID
from users.models import User

from .serializers import GoogleAuth


def check_google_auth(google_user: GoogleAuth) -> dict:
    """Checks authentication for Google"""
    try:
        id_token.verify_oauth2_token(
            google_user["token"], requests.Request(), GOOGLE_CLIENT_ID
        )
    except ValueError:
        raise AuthenticationFailed(code=403, detail="bad token google")

    user, created = User.objects.get_or_create(email=google_user["email"])

    return create_token(user.id)


def create_token(user_id: int) -> dict:
    """create token"""
    access_token_expires = timedelta(minutes=60 * 24)
    return {
        "user_id": user_id,
        "access_token": create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expires
        ),
        "token_type": "Token",
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """create access token"""
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": "access"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt

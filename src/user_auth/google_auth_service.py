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

    try:
        user = User.objects.get(email=google_user["email"])
        if not user.is_google_auth:
            raise AuthenticationFailed(
                code=403, detail="User already registered with email and password"
            )
    except User.DoesNotExist:
        user = User.objects.create(email=google_user["email"], is_google_auth=True)

    return create_token(user.id)


def create_token(user_id: int) -> dict:
    """create token"""
    access_token_expires = timedelta(minutes=60 * 24)
    expire = datetime.utcnow() + access_token_expires
    to_encode = {"user_id": user_id, "exp": expire, "sub": "access"}
    access_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return {
        "user_id": user_id,
        "access_token": access_token,
    }

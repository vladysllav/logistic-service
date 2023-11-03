from datetime import datetime, timedelta
from enum import Enum

import jwt
from django.conf import settings
from django.core.mail import send_mail


class RegEx(Enum):
    """create a class with regular expressions for validators in models"""

    PASSWORD = (
        r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$",
        [
            "password must contain 1 number (0-9)",
            "password must contain 1 uppercase letter",
            "password must contain 1 lowercase letter",
            "password must contain 1 non-alpha numeric",
            "password min 8 max 20 ch",
        ],
    )

    NAME = (r"^[a-zA-Z]{2,20}$", "only letters min 2 max 20 ch")

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg


def send_invitation_email(email, token):
    subject = "Invitation to Join"
    message = (
        f"You have been invited to join. Please click the link to activate your account:"
        f" http://127.0.0.1:8000/api/users/accept-invitation/{token}"
    )
    from_email = "talk.team.challenge@gmail.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


def generate_activation_token(self):
    """generate toker for users when superuser send invite"""
    return jwt.encode(
        {"user_id": self.pk, "exp": datetime.utcnow() + timedelta(days=1)},
        settings.SECRET_KEY,
        algorithm="HS256",
    )

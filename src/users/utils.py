from enum import Enum


class RegEx(Enum):
    """create a class with regular expressions for validators in models"""
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\s])[^\s]{8,20}$',
        [
            'password must contain 1 number (0-9)',
            'password must contain 1 uppercase letter',
            'password must contain 1 lowercase letter',
            'password must contain 1 non-alpha numeric',
            'password min 8 max 20 ch'
        ]
    )

    NAME = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg

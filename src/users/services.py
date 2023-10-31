from typing import List

from users.models import User
from users.repositories import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users_list(self) -> List[User]:
        return self.user_repository.get_users_list()

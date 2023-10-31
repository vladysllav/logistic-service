from abc import ABC, abstractmethod
from typing import List

from users.models import User


class UserRepository(ABC):
    @abstractmethod
    def get_users_list(self) -> List[User]:
        pass


class DatabaseUserRepository(UserRepository):
    def get_users_list(self) -> List[User]:
        return User.objects.all()

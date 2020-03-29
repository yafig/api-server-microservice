from abc import ABC, abstractmethod
from repository.database_interface import DatabaseInterface
from repository.user_model import User

class UserServiceInterface(ABC):
    @abstractmethod
    def get_user(self, username: str):
        pass

    @abstractmethod
    def register(self, email: str, username: str, password: str) -> User:
        pass
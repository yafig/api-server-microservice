from abc import ABC, abstractmethod
from repository.database_interface import DatabaseInterface
from repository.user_model import User

SECRET_KEY = "random string"

class UserServiceInterface(ABC):
    @abstractmethod
    def get_user(self, username: str):
        pass

    @abstractmethod
    def register(self, email: str, username: str, password: str) -> User:
        pass

    @abstractmethod
    def login(self, username: str, raw_password: str) -> str:
        pass

    @abstractmethod
    def edit_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, username: str) -> bool:
        pass

from abc import ABC, abstractmethod
from typing import Optional, List
from .user_model import User

class DatabaseInterface(ABC):
    @abstractmethod
    def find_user(self, email: Optional[str] = None, username: Optional[str] = None) -> User:
        pass

    @abstractmethod
    def add_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def delete_user(self, username: str) -> bool:
        pass

    @abstractmethod
    def edit_user(self, user: User) -> User:
        pass
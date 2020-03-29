from abc import ABC, abstractmethod
from typing import Optional, List
from .user_model import User

class DatabaseInterface(ABC):
    @abstractmethod
    def find_user(self, email: str, username: str) -> User:
        pass

    @abstractmethod
    def add_user(self, username: str):
        pass

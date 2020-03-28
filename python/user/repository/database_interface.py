from abc import ABC, abstractmethod
from typing import Optional, List
from .user_model import User

class DatabaseInterface(ABC):
    @abstractmethod
    def get_user(self, username: str) -> User:
        pass

    @abstractmethod
    def add_user(self, username: str):
        pass

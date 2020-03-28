from abc import ABC, abstractmethod
from repository.database_interface import DatabaseInterface

class UserServiceInterface(ABC):
    @abstractmethod
    def get_user(self, username: str):
        pass
    
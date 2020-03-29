from repository.database_interface import DatabaseInterface
from .user_service_interface import UserServiceInterface
from repository.user_model import User
from injector import inject

class UserService(UserServiceInterface):
    @inject
    def __init__(self, db: DatabaseInterface):
        self.db = db
    
    def get_user(self, username: str) -> User:
        user = self.db.get_user(username)
        return user
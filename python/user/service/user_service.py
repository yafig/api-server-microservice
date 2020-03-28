from repository.database_interface import DatabaseInterface
from .user_service_interface import UserServiceInterface
from injector import inject

class UserService(UserServiceInterface):
    @inject
    def __init__(self, db: DatabaseInterface):
        self.db = db
    
    def get_user(self, username: str):
        return username
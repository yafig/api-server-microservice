from repository.database_interface import DatabaseInterface
from .user_service_interface import UserServiceInterface
from repository.user_model import User
from injector import inject
from helper import hash_password, randomString

class UserService(UserServiceInterface):
    @inject
    def __init__(self, db: DatabaseInterface):
        self.db = db
       
    def register(self, email: str, username: str, password: str) -> User:
        if self.db.find_user(username=username):
            raise Exception({"error_message": "Username is already taken"})

        if self.db.find_user(email=email):
            raise Exception({"error_message": "Email is already registered"})

        salt = randomString(32)
        hashed_password = hash_password(password, salt)
        user = User(None, username, email, None, hashed_password, salt)
        self.db.add_user(user)
        return user

    def get_user(self, username: str) -> User:
        user = self.db.find_user(username=username)
        return user

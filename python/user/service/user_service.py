from repository.database_interface import DatabaseInterface
from .user_service_interface import UserServiceInterface, SECRET_KEY
from repository.user_model import User
from injector import inject
from helper import hash_password, randomString
import jwt

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
        return self.get_user(username=username)

    def login(self, username: str, raw_password: str) -> str:
        if user := self.get_user(username=username):
            if hash_password(raw_password, user.password_salt).decode() == user.password:
                payload = {"username": user.username, "fullname": user.fullname, "status": user.status}
                token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                return token.decode()

    def get_user(self, username: str) -> User:
        user = self.db.find_user(username=username)
        return user

    def edit_user(self, username: str, user: User) -> bool:
        return True

    def delete_user(self, username: str) -> bool:
        # TODO: Run grpc call to Post service
        return self.db.delete_user(username)


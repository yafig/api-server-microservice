from typing import Optional, List
import sqlalchemy
from .user_model import User

from .database_interface import DatabaseInterface

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                        sqlalchemy.Column("username", sqlalchemy.Text),
                        sqlalchemy.Column("email", sqlalchemy.Text),
                        sqlalchemy.Column("fullname", sqlalchemy.Text),
                        sqlalchemy.Column("password", sqlalchemy.Text),
                        sqlalchemy.Column("password_salt", sqlalchemy.Text),
                        sqlalchemy.Column("status", sqlalchemy.Text)
                        )

class MySQLAdapter(DatabaseInterface):
    def __init__(self, database_uri: str) -> None:
        engine = sqlalchemy.create_engine(database_uri)
        self.__connection = engine.connect()

    def find_user(self, email: Optional[str] = None, username: Optional[str] = None) -> User:
        if email and username:
            query = users.select().where(users.c.username == username and users.c.email == email)
        elif email and not username:
            query = users.select().where(users.c.email == email)
        elif username and not email:
            query = users.select().where(users.c.username == username)
        else:
            raise Exception("Invalid find query")

        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        if row:
            return User(**row)
        else:
            return None

    def add_user(self, user: User) -> User:
        query = users.insert().values(
                                        username=user.username,
                                        email=user.email,
                                        password=user.password,
                                        password_salt=user.password_salt,
                                        status=user.status
                                    )
        self.__connection.execute(query)
        return self.find_user(username=user.username)

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

    def get_user(self, username: str) -> User:
        query = users.select().where(users.c.username == username)
        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        print(row)
        return User(**row)

    def add_user(self, username: str):
        pass

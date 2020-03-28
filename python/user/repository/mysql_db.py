from typing import Optional, List
import sqlalchemy
from .user_model import User

from .database_interface import DatabaseInterface

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
                        )

class MySQLAdapter(DatabaseInterface):
    def __init__(self, database_uri: str) -> None:
        pass
        # engine = sqlalchemy.create_engine(database_uri)
        # self.__connection = engine.connect()

    def get_user(self, username: str) -> User:
        pass
    #     query = users.select().where(users.c.username == username)
    #     cursor = self.__connection.execute(query)
    #     row = cursor.fetchone()
    #     return User(**row)

    def add_user(self, username: str):
        pass

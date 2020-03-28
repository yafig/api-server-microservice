from injector import singleton
from repository.database_interface import DatabaseInterface
from repository.mysql_db import MySQLAdapter
from service.user_service_interface import UserServiceInterface
from service.user_service import UserService
import os

MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
MYSQL_HOST =  os.environ.get("MYSQL_HOST", "mysql")
MYSQL_TABLE = os.environ.get("MYSQL_TABLE", "yafig")
MYSQL_URI = f"mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_TABLE}"

def configure(binder):
    binder.bind(UserServiceInterface, to=UserService, scope=singleton)
    binder.bind(DatabaseInterface, to=MySQLAdapter(MYSQL_URI), scope=singleton)

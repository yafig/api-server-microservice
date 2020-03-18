from sqlalchemy_utils import create_database, database_exists, drop_database
from app import create_app
from models import db, User

app = create_app()
app.app_context().push()

def create_db():
    url = app.config["SQLALCHEMY_DATABASE_URI"]
    if database_exists(url):
        drop_database(url)

    create_database(url)
    db.create_all()

if __name__ == '__main__':
    create_db()
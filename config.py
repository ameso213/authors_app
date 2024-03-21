from app.extensions import db
from datetime import datetime
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/authors'
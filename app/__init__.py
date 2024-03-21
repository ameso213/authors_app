from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.extensions import db, migrate
from flask_bcrypt import Bcrypt
from app.extensions import bcrypt

from app.controllers.auth_controller import auth
from app.controllers.book_controller import book
from app.controllers.company_controller import company




# db = SQLAlchemy()
# migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize SQLAlchemy and Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import models
    from app.models import users
    from app.models import books
    from app.models import companies

    @app.route('/')
    def home():
        return "Hello programmers"
    
    #import blue prints
    from app.controllers.auth_controller import auth
    from app.controllers.company_controller import company
    from app.controllers.book_controller import book

    #register blue prints
    app.register_blueprint(auth,url_prefix='/api/v1/auth')
    app.register_blueprint(company,url_prefix='/api/v1/company')
    app.register_blueprint(book,url_prefix='/api/v1/book')


    return app

if __name__ == "__main__":
    app = create_app()
    app.run()




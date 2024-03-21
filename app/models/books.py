from app import db
from datetime import datetime

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Float, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    publication_date = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(30), nullable=False, unique=True)
    genre = db.Column(db.String(50), nullable=False)
    company_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __init__(self, title, description, price, pages, publication_date, isbn, genre, company_id):
        self.title = title
        self.description = description
        self.price = price
        self.pages = pages
        self.publication_date = publication_date
        self.isbn = isbn
        self.genre = genre
        self.company_id = company_id

    def save(self):
        # Adding and committing to the database
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            # If there's an integrity error, return a specific error message
            return {"error": str(e)}, 400

        # Building a response message
        return {"message": f"Book '{self.title}', ID '{self.id}' has been uploaded"}, 201

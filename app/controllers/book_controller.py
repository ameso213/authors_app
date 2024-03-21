from flask import Blueprint, request, jsonify
from app.models.books import Book  # Import the Book model
from app import db

book = Blueprint('book', __name__, url_prefix='/api/v1/book')

@book.route('/register', methods=['POST'])
def register_book():
    try:
        # Extracting request data
        data = request.json
        print("Request Data:", data)  # Debug statement to print request data
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        pages = data.get('pages')
        publication_date = data.get('publication_date')
        isbn = data.get('isbn')
        genre = data.get('genre')
        company_id = data.get('company_id')

        # Basic input validation
        if not all([title, description, price, pages, publication_date, isbn, genre, company_id]):
            print("Missing Required Fields:", title, description, price, pages, publication_date, isbn, genre)  # Debug statement to print missing fields
            return jsonify({"error": 'All fields are required'}), 400

        # Creating a new book
        new_book = Book(
            title=title,
            description=description,
            price=float(price),
            pages=int(pages),
            publication_date=publication_date,
            isbn=isbn,
            genre=genre,
            company_id=int(company_id)
        )

        # Adding and committing to the database
        db.session.add(new_book)
        db.session.commit()

        # Building a response message
        return jsonify({"message": f"Book '{new_book.title}', ID '{new_book.id}' has been uploaded"}), 201

    except Exception as e:
        # Handle exceptions appropriately
        return jsonify({"error": str(e)}), 500

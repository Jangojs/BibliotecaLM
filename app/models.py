from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200))  # URL of the book's image

    def __repr__(self):
        return f'<Book {self.title}>'

class BookSearch(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(30), nullable=False)

class AddBook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    publication_year = db.Column(db.Date, nullable=False)

class UpdateBookInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    publication_year = db.Column(db.Date, nullable=False)

class DeleteBook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    search_id = db.Column(db.Integer, db.ForeignKey('book_search.id'), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    publication_year = db.Column(db.Date, nullable=False)


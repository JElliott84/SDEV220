from flask import Flask
app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(200))

    def __repr__(self):
        return f"{self.name} - {self.description}" 

@app.route('/')
def index():
    return 'Hello!'

@app.route('/book')
def get_book():
    books = Book.query.all()
    output = []
    for book in books:
        drink_data = {'name': Book.bookname, 'Author': Book.author, 'Publisher': Book.publisher}
        output.append(drink.data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": Book.bookname, "Author": Book.author, "Publisher": Book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['Bookname'], author=request.json['author'])
    db.seesion.add(book)
    db.seesion.commit()
    return {'id':book.id}
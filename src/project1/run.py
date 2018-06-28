from book_app import app
from book_app import db
if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
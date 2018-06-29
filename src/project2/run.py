from slack_app import app
from slack_app import db
if __name__ == '__main_':
    # db.create_all()
    app.run(debug=True)
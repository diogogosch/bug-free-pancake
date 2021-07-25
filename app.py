from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
db.init_app(app)
from views import *


def init_db():
    db.create_all()


# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=models.db)


if __name__ == '__main__':
    app.run(debug=True)
    init_db()

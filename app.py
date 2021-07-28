from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy()
engine = create_engine('mysql://user:password@localhost/my-db', echo=True)
from controller import *

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)


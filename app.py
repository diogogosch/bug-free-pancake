from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
# app.config.from_pyfile('config.py')
engine = create_engine('mysql://user:password@localhost/my-db', echo=True)
Session = sessionmaker(bind=engine)

from controller import *

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)


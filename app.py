from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
engine = create_engine('mysql://root:password@0.0.0.0:3306/my-db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

from controller import *

if __name__ == '__main__':
    app.run(debug=True)

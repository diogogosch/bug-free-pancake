from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cryptography.fernet import Fernet

app = Flask(__name__)
engine = create_engine('mysql://root:password@0.0.0.0:3306/my-db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def generate_key():
    # Generates key and saves to file
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    # Loads the secret key
    return open("secret.key", "rb").read()


from controller import *

if __name__ == '__main__':
    app.run(debug=True)
    # generate_key()

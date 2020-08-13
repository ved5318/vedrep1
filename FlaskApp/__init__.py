from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '@12345678@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskdb'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


consumer_token='AyeMkToNVdtICkcXSynim0ASn'
consumer_secret='ec4ffvb8SLaC79U080hyqWR0oqxWmcNM7iollCuoTrikIfhIbs'

from FlaskApp import routes
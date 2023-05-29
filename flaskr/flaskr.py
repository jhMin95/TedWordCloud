# all the imports
from flask import Flask, request, session, redirect, url_for, \
     abort, render_template, flash, current_app, g
import psycopg2, psycopg2.extras
from flask_sqlalchemy import SQLAlchemy

# create our little application :)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jimin:eodid9978$@localhost:5432/jimin'

db = SQLAlchemy(app)

@app.route('/')
def index():
    if db.session.connection():
        return 'DB connection SUCCEED!!! :)'
    else:
        return 'DB connection failed... :('

if __name__ == '__main__':
    app.run(debug=True)


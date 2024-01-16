from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'AOHDNBIAAI189SD!A1'

# postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2305@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from api.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

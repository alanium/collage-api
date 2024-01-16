from flask import Flask
from flask_cors import CORS
from models.data import db


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'AOHDNBIAAI189SD!A1'

# postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2305@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crea las tablas si no existen
with app.app_context():
    db.create_all()


from api.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




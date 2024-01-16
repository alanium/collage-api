from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)

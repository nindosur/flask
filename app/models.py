from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255))
    phone = db.Column(db.String(20), nullable=False)

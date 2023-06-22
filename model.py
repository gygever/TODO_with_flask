from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    content = db.Column(db.String(255))

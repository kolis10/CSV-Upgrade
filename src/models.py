from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Tournaments(db.Model):
    __tablename__ = 'tournaments'
    id = db.Column(db.Integer, primary_key=True)
    casino = db.Column(db.String(40))
    name = db.Column(db.String(500), nullable=False)
    h1 = db.Column(db.String(200))
    buy_in = db.Column(db.String(20))
    blinds = db.Column(db.String(20))
    starting_stack = db.Column(db.String(20))
    results_link = db.Column(db.String(500))
    structure_link = db.Column(db.String(500))
    start_at = db.Column(db.DateTime)
    notes = db.Column(db.String(3000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Tournaments %r>' % self.name

    def serialize(self):
        return {
            "date" : self.date,                       # 0, 1
            "casino" : self.casino,                   # 3
            "name": self.name,                        # 4
            "buy_in": self.buy_in,                    # 5
            "blinds" : self.blinds,                   # 7
            "starting_stack" : self.starting_stack,   # 6
            "results_link" : self.results_link,       # 13
            "structure_link" : self.structure_link,   # 8
            "start_at" : self.start_at,               # datetime 0, 2
            "notes" : self.notes,                     # 12
            "created_at" : self.created_at,           #
            "updated_at" : self.updated_at            #
        }

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }
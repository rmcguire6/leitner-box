from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    cards = db.relationship('Card', backref='creator', lazy='dynamic')
    def __repr__(self):
        return '<User {}'.format(self.username)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(64), required=True)
    question = db.Column(db.String(64), required=True)
    answer = db.Column(db.String(64), required=True)
    active = db.Column(db.Boolean, default=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Card {}'.format(self.question)

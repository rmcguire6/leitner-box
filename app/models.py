from app import db, ma

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    cards_per_day = db.Column(db.Integer, nullable=False)
    cards = db.relationship('Card', backref='user', lazy='select')
    def __repr__(self):
        return '<User {}'.format(self.username)
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'username', 'cards_per_day')

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(64), nullable=False)
    question = db.Column(db.String(64), nullable=False)
    answer = db.Column(db.String(64), nullable=False)
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    def __repr__(self):
        return '<Card {}'.format(self.question)

class CardSchema(ma.Schema):
    class Meta:
        fields = ('card_id', 'subject', 'question', 'answer','active', 'user_id')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

card_schema = CardSchema()
cards_schema = CardSchema(many=True)

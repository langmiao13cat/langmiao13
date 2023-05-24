from extensions import db
from datetime import datetime


class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(50), db.ForeignKey('user.line_id'))
    birthday = db.Column(db.Date)
    joined_on = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, line_id, birthday):
        self.line_id = line_id
        self.birthday = birthday

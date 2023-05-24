from extensions import db
import datetime


class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.line_id'))
    gift_category = db.Column(db.String(255))  # 禮物類別
    gift_title = db.Column(db.String(255))  # 禮物標題
    birthday = db.Column(db.Date)  # 生日日期
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())  # 預約建立時間

    def __init__(self, user_id, gift_category, gift_title, birthday):
        self.user_id = user_id
        self.gift_category = gift_category
        self.gift_title = gift_title
        self.birthday = birthday

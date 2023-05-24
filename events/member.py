from line_bot_api import line_bot_api
from models.user import User
from models.member import Member
from extensions import db
from linebot.models import *
from datetime import datetime


def handle_member_registration(event):
    line_id = event.source.user_id

    # 檢查用戶是否已存在
    user = User.query.filter_by(line_id=line_id).first()
    if user:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="您已是會員")
        )
        return

    # 創建用戶並提交資料庫
    user = User(line_id=line_id, display_name="", picture_url="")
    db.session.add(user)
    db.session.commit()

    # 創建會員並提交資料庫
    member = Member(line_id=line_id, birthday=None)
    db.session.add(member)
    db.session.commit()

    # 產生確認模板
    confirm_template = ConfirmTemplate(
        text="加入會員",
        actions=[
            PostbackAction(label="是", data="join_member"),
            MessageAction(label="否", text="不，我暫時不想加入")
        ]
    )

    # 回覆確認模板
    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(alt_text="加入會員確認", template=confirm_template)
    )


def handle_membership_confirmation(event):
    # 處理會員確認事件的函數
    line_id = event.source.user_id
    message_text = event.message.text

    # 檢查用戶是否已存在
    user = User.query.filter_by(line_id=line_id).first()
    if not user:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="您尚未加入會員")
        )
        return

    if message_text == "是":
        # 請回應您的暱稱
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請回覆您的暱稱")
        )
    elif message_text == "否":
        # 不加入會員
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="感謝您的回覆")
        )


def handle_user_nickname(event):
    # 處理用戶回覆暱稱的函數
    line_id = event.source.user_id
    nickname = event.message.text

    # 更新用戶的暱稱
    user = User.query.filter_by(line_id=line_id).first()
    user.display_name = nickname
    db.session.commit()

    # 跳出日期選擇器
    date_picker = DatetimePickerAction(
        label="請選擇您的生日",
        data="choose_birthday",
        mode="date"
    )

    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text="選擇生日",
            template=ButtonsTemplate(
                text="請選擇您的生日",
                actions=[date_picker]
            )
        )
    )


def handle_birthday_selection(event):
    # 處理用戶選擇生日的函數
    line_id = event.source.user_id
    birthday = event.postback.params["date"]

    # 更新用戶的生日
    member = Member.query.filter_by(line_id=line_id).first()
    member.birthday = birthday
    db.session.commit()

    # 回覆用戶成為會員的訊息
    user = User.query.filter_by(line_id=line_id).first()
    nickname = user.display_name
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"恭喜 {nickname} 已經成為會員，您的生日是 {birthday}")
    )

    # 詢問用戶是否確認生日
    confirm_template = ConfirmTemplate(
        text="您的生日正確嗎?",
        actions=[
            PostbackAction(label="是", data="confirm_birthday"),
            MessageAction(label="否", text="不，我要重新選擇生日")
        ]
    )

    line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(alt_text="生日確認", template=confirm_template)
    )


def handle_birthday_confirmation(event):
    # 處理生日確認事件的函數
    line_id = event.source.user_id
    message_text = event.message.text

    if message_text == "是":
        # 根據用戶的生日當月一號發送生日快樂和特殊優惠訊息
        member = Member.query.filter_by(line_id=line_id).first()
        birthday = member.birthday

        send_birthday_message(member)  # 呼叫發送生日訊息的函數

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="已確認您的生日")
        )
    elif message_text == "否":
        # 重新選擇生日
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請重新選擇您的生日")
        )


def send_birthday_message(member):
    # 根據用戶的生日當月一號發送生日快樂和特殊優惠訊息
    current_month = datetime.now().month
    current_day = datetime.now().day

    if member.birthday.month == current_month and current_day == 1:
        nickname = member.user.display_name
        birthday_coupon = generate_birthday_coupon()

        message = f"{nickname}生日快樂，浪喵果乾舖送上專屬您的生日優惠碼 {birthday_coupon}"
        line_bot_api.push_message(member.user.line_id, TextSendMessage(text=message))


def generate_birthday_coupon():
    return "Habby_birthday13"


def handle_unsubscribe(event):
    line_id = event.source.user_id

    # 檢查用戶是否存在於資料庫
    user = User.query.filter_by(line_id=line_id).first()
    if not user:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="您尚未加入會員")
        )
        return

    # 在這裡實現用戶退出會員的相關邏輯
    # 可以從資料庫中刪除用戶相關的資料或標記用戶為非會員狀態

    # 回覆用戶退出會員的訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="已成功退出會員")
    )

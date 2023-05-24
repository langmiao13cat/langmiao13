from flask import Flask, request, abort
from events.basic import *
from events.product import *
from events.product2 import *
from events.member import *
from urllib.parse import parse_qsl
from line_bot_api import *
from extensions import db, migrate
from models.member import Member
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:migo520@localhost:5432/cat13'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)
migrate.init_app(app, db)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = str(event.message.text).lower()

    user = User.query.filter(User.line_id == event.source.user_id).first()

    if not user:
        profile = line_bot_api.get_profile(event.source.user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)

        user = User(profile.user_id, profile.display_name, profile.picture_url)
        db.session.add(user)
        db.session.commit()

    print(user.id)
    print(user.line_id)
    print(user.display_name)

    if message_text == "加入會員":
        handle_member_registration(event)
        handle_membership_confirmation(event)
        handle_user_nickname(event)
        handle_birthday_selection(event)
        handle_birthday_confirmation(event)

    elif message_text == "退出會員":
        handle_unsubscribe(event)

    if message_text == '@關於浪喵果乾舖':
        column_quick_reply_event(event)

    if message_text == '@浪喵賦予的新生命':
        store3_event(event)

    elif message_text == '貓奴一定要吃天然水果乾':
        product_category_event(event)

    elif message_text == '專屬貓奴的罐裝水果乾':
        product2_category_event(event)

    elif message_text == '@浪喵果乾舖官網與其他賣場':
        store_event(event)

    elif message_text == '@米麒麟浪喵生活館':
        store2_event(event)

    elif message_text == '@呼叫貓奴':
        deallocating13_event(event)

    elif message_text == '貓奴講故事吧':
        about_us_event(event)

    elif message_text == '浪喵果乾禮盒系列':
        stop1_event(event)

    elif message_text == '貓奴必備文創小物':
        stop2_event(event)

    elif message_text == '貓奴私藏的精選美食':
        stop3_event(event)

    elif message_text == '米麒麟·漿樣子喝果乾水':
        stop4_event(event)

    elif message_text == '米麒麟毛孩生活館':
        stop5_event(event)

    elif message_text == '客製化專屬於您的故事':
        stop6_event(event)

    elif message_text == '@最新優惠與優惠券領取':
        deallocating_event(event)

    if message_text in ['念念是一隻三花貓', '墨墨是一隻黑貓', 'HOYA是一隻吃貨虎斑貓',
                        'TIMI是一隻白底虎斑貓', '宅宅是一隻灰虎斑貓',
                        '炭炭是一隻虎斑花貓', '阿布拉是一隻賓士貓',
                        '米香是一隻閃電尾白貓', '米樂是一隻藍眼白貓',
                        '米多是一隻天花板上的灰虎斑貓', 'MIGO是一隻天使白貓',
                        'HOYA是一隻好野貓', 'FIRA是一隻玳瑁貓', '胖妲是一隻賓士貓']:
        cat_intro(event)


@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))

    # 取出動作類型
    action = data.get('action')

    if action == 'category':
        product_category_event(event)
    elif action == 'product2':
        product2_event(event)
    elif action == 'select_date':
        product_event(event)
    elif action == 'product':
        product_event(event)
    elif action == 'product2_category':
        product2_category_event(event)
    elif action == 'join_member':
        handle_member_registration(event)
    elif action == 'choose_nickname':
        handle_user_nickname(event)
    elif action == 'choose_birthday':
        handle_birthday_selection(event)
    elif action == 'confirm_birthday':
        handle_birthday_confirmation(event)

    print('action:', action)
    print('category:', data.get('category'))
    print('product_id:', data.get('product_id'))
    print('product2_id:', data.get('product2_id'))


@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """喵~歡迎來到「浪喵果乾舖」:)

用13隻流浪貓的名子，
賦予每一款果乾新生命。

相信您也有與貓相遇的故事，
歡迎分享給我們唷。

浪喵果乾舖秉持著，
天然水果不添加防腐劑、色素，
純天然手工低溫烘焙製作，
讓每一個果乾保留原始滋味，
酸甜滋味一口就愛上，
您購買的每一包果乾，
都幫您捐5%給浪浪機構。

各位「喵果粉」們，
都可以留言貓奴互動喔~
也可以直接點選下方【選單功能】
我們期待與您一起大口吃果乾，
浪愛延續下去！"""

    image_url = "https://i.imgur.com/nhuLjIy.png"  # 替換成您自己的圖片網址
    image_message = ImageSendMessage(original_content_url=image_url, preview_image_url=image_url)

    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=welcome_msg), image_message]
    )


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


if __name__ == "__main__":
    app.run()

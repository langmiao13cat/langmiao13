from urllib.parse import parse_qsl

from line_bot_api import *

products = {
    1: {
        'category': '情人果系列',
        'title': '情人果乾系列',
        'img_url': 'https://i.imgur.com/alWby9K.png',
        'project': '「念念」不忘情人果乾',
        'price': 185,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/795814/3136817/1',
        'cat_name': '「念念」',
        'message': '念念是一隻三花貓',
    },
    2: {
        'category': '情人果系列',
        'title': '情人果乾系列',
        'img_url': 'https://i.imgur.com/1s8AvHZ.png',
        'project': '偷偷「墨墨」加點梅情人果乾',
        'price': 185,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/796527/3136820/1',
        'cat_name': '「墨墨」',
        'message': '墨墨是一隻黑貓',
    },
    3: {
        'category': '芭樂乾系列',
        'title': '芭樂乾系列',
        'img_url': 'https://i.imgur.com/8QC3Bh2.png',
        'project': '「宅」熱愛喜芭樂乾',
        'price': 160,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/796533/3136821/1',
        'cat_name': '「宅宅」',
        'message': '宅宅是一隻灰虎斑貓',
    },
    4: {
        'category': '芭樂乾系列',
        'title': '芭樂乾系列',
        'img_url': 'https://i.imgur.com/KQ19IW4.png',
        'project': '「TIMI」梅事也愛鬥熱鬧芭樂乾',
        'price': 160,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/796533/3136821/1',
        'cat_name': '「TIMI」',
        'message': 'TIMI是一隻白底虎斑貓',

    },
    5: {
        'category': '芒果乾系列',
        'title': '芒果乾系列',
        'img_url': 'https://i.imgur.com/pKnhzIk.png',
        'project': '「炭」頭「炭」尾無糖芒果乾',
        'price': 220,
        'weight': 130,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/810324/3135063/1',
        'cat_name': '「炭炭」',
        'message': '炭炭是一隻虎斑花貓',

    },
    6: {
        'category': '芒果乾系列',
        'title': '芒果乾系列',
        'img_url': 'https://i.imgur.com/Yvl3w0i.png',
        'project': '「阿布拉」愛吻愛聞微糖芒果乾',
        'price': 220,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/818250/3136725/1',
        'cat_name': '「阿布拉」',
        'message': '阿布拉是一隻賓士貓',

    },
    7: {
        'category': '米麒麟系列',
        'title': '米麒麟系列',
        'img_url': 'https://i.imgur.com/uKcNScy.png',
        'project': '「米」麒麟芳「香」四溢洛神花',
        'price': 175,
        'weight': 130,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/968682/2571518/1',
        'cat_name': '「米香」',
        'message': '米香是一隻閃電尾白貓',

    },
    8: {
        'category': '米麒麟系列',
        'title': '米麒麟系列',
        'img_url': 'https://i.imgur.com/uE6ntQA.png',
        'project': '「米」麒麟紅心芭「樂」乾',
        'price': 175,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/810278/2171802/1',
        'cat_name': '「米樂」',
        'message': '米樂是一隻藍眼白貓',

    },
    9: {
        'category': '米麒麟系列',
        'title': '米麒麟系列',
        'img_url': 'https://i.imgur.com/R4KWFHJ.png',
        'project': '「米」麒麟營養「多」多蔓越莓乾',
        'price': 175,
        'weight': 170,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1013111/2677643/1',
        'cat_name': '「米多」',
        'message': '米多是一隻天花板上的灰虎斑貓',
    },
    10: {
        'category': '柑橘檬系列',
        'title': '柑橘檬系列',
        'img_url': 'https://i.imgur.com/DtQv149.png',
        'project': '「MIGO」來去兜風檸檬乾',
        'price': 180,
        'weight': 90,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1367928/3632384/1',
        'cat_name': '「MIGO」',
        'message': 'MIGO是一隻天使白貓',
    },
    11: {
        'category': '柑橘檬系列',
        'title': '柑橘檬系列',
        'img_url': 'https://i.imgur.com/DtQv149.png',
        'project': '「HOYA」橘翔如意橘子乾',
        'price': 165,
        'weight': 140,
        'post_url': 'https://i.imgur.com/0PhCpXq.png',
        'cat_name': '「HOYA」',
        'message': 'HOYA是一隻好野貓',
    },
    12: {
        'category': '鳳梨乾系列',
        'title': '鳳梨乾系列',
        'img_url': 'https://i.imgur.com/vLx2xhm.png',
        'project': '「FIRA」出門溜搭吃柳橙乾',
        'price': 175,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/821897/2201613/1',
        'cat_name': '「FIRA」',
        'message': 'FIRA是一隻玳瑁貓',
    },
    13: {
        'category': '鳳梨乾系列',
        'title': '鳳梨乾系列',
        'img_url': 'https://i.imgur.com/xTGvvnz.png',
        'project': '「HOYA」好野旺旺無糖鳳梨乾',
        'price': 160,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/797226/3136825/1',
        'cat_name': '「HOYA」',
        'message': 'HOYA是一隻吃貨虎斑貓',
    },
    14: {
        'category': '柑橘檬系列',
        'title': '柑橘檬系列',
        'img_url': 'https://i.imgur.com/StjnHW1.png',
        'project': '「胖妲」出門溜噠柳橙乾',
        'price': 160,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1105475/2935901/1',
        'cat_name': '「胖妲」',
        'message': '胖妲是一隻賓士貓',
    },
}


def product_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='用浪喵的名子，賦予的果乾新生命',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/ix97EdK.png',
                    action=PostbackAction(
                        label='情人果系列',
                        display_text='情人果系列',
                        data='action=product&category=情人果系列'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/8gOfK6p.png',
                    action=PostbackAction(
                        label='芭樂乾系列',
                        display_text='芭樂乾系列',
                        data='action=product&category=芭樂乾系列'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/OJQWSOe.png',
                    action=PostbackAction(
                        label='鳳梨乾系列',
                        display_text='鳳梨乾系列',
                        data='action=product&category=鳳梨乾系列'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/lWXc02A.png',
                    action=PostbackAction(
                        label='芒果乾系列',
                        display_text='芒果乾系列',
                        data='action=product&category=芒果乾系列'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/1thm2Lp.png',
                    action=PostbackAction(
                        label='米麒麟系列',
                        display_text='米麒麟系列',
                        data='action=product&category=米麒麟系列'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/li6L23e.png',
                    action=PostbackAction(
                        label='柑橘檬系列',
                        display_text='柑橘檬系列',
                        data='action=product&category=柑橘檬系列'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/vFL5Ny2.png',
                    action=MessageAction(
                        label='重新開始',
                        text="@浪喵賦予的新生命"
                    )
                ),
            ]
        )
    )

    line_bot_api.reply_message(
        event.reply_token,
        image_carousel_template_message)


def product_event(event):
    data = dict(parse_qsl(event.postback.data))
    category = data['category']

    # 創建一個空的列表來存放符合類別的氣泡資訊
    bubbles = []

    for product_id, product in products.items():
        if product['category'] == category:
            # 將符合類別的商品資訊轉換為氣泡格式並加入列表
            bubble = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "12:12",
                    "aspectMode": "fit",
                    "url": product['img_url']
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "text",
                            "text": product['title'],
                            "wrap": True,
                            "weight": "bold",
                            "size": "xl",
                            "color": "#A48E7E"
                        },
                        {
                            "type": "text",
                            "text": product['project'],
                            "align": "start",
                            "color": "#A48E7E",
                            "size": "md"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "separator",
                                    "margin": "md",
                                    "color": "#FFFDF8"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": '重量     {}g'.format(product['weight']),
                                            "weight": "regular",
                                            "size": "md",
                                            "flex": 2,
                                            "color": "#A48E7E",
                                            "align": "start",
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": '價錢       ${}'.format(product['price']),
                                            "weight": "regular",
                                            "size": "md",
                                            "color": "#A48E7E",
                                            "align": "start",
                                            "flex": 2
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "backgroundColor": "#FFFDF8"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "none",
                    "contents": [
                        {
                            "type": "button",
                            "style": "primary",
                            "action": {
                                "type": "uri",
                                "label": "添加到網站購物車",
                                "uri": product['post_url']
                            },
                            "color": "#A48E7E",
                            "height": "sm"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "postback",
                                "label": "進一步認識{}".format(product['cat_name']),
                                "data": f"action=select_date&product_id={product_id}&category={product['category']}",
                                "text": product['message'],
                            },
                            "color": "#EDE3DB",
                            "height": "sm",
                            "style": "primary"
                        }
                    ],
                    "backgroundColor": "#EDE3DB",
                    "borderColor": "#EDE3DB"
                },
                "styles": {
                    "header": {
                        "backgroundColor": "#FFFDF8"
                    },
                    "footer": {
                        "backgroundColor": "#EDE3DB"
                    }
                }
            }

            bubbles.append(bubble)

    # 將氣泡列表轉換為 FlexMessage 並回覆給使用者
    flex_message = FlexSendMessage(
        alt_text='請選擇果乾類別',
        contents={
            "type": "carousel",
            "contents": bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message]
    )


def cat_intro(event):
    message_text = str(event.message.text).lower()

    if message_text == '念念是一隻三花貓':
        message = TextSendMessage(text='念念是一隻三花貓')
        cat_image_url = 'https://i.imgur.com/uLPeYmo.jpg'

    elif message_text == '墨墨是一隻黑貓':
        message = TextSendMessage(text='墨墨是一隻黑貓')
        cat_image_url = 'https://i.imgur.com/GonaC9I.jpg'

    elif message_text == 'HOYA是一隻吃貨虎斑貓':
        message = TextSendMessage(text='HOYA是一隻吃貨虎斑貓')
        cat_image_url = 'https://i.imgur.com/PvSiMkD.jpg'

    elif message_text == 'TIMI是一隻白底虎斑貓':
        message = TextSendMessage(text='TIMI是一隻白底虎斑貓')
        cat_image_url = 'https://i.imgur.com/PCIfsyE.jpg'

    elif message_text == '宅宅是一隻灰虎斑貓':
        message = TextSendMessage(text='宅宅是一隻灰虎斑貓')
        cat_image_url = 'https://i.imgur.com/MfCMOXb.png'

    elif message_text == '炭炭是一隻虎斑花貓':
        message = TextSendMessage(text='炭炭是一隻虎斑花貓')
        cat_image_url = 'https://i.imgur.com/8Ao1fxZ.jpg'
    elif message_text == '阿布拉是一隻賓士貓':
        message = TextSendMessage(text='阿布拉是一隻賓士貓')
        cat_image_url = 'https://i.imgur.com/JeWdhSA.jpg'

    elif message_text == '米香是一隻閃電尾白貓':
        message = TextSendMessage(text='米香是一隻閃電尾白貓')
        cat_image_url = 'https://i.imgur.com/wfQVxYK.jpg'

    elif message_text == '米樂是一隻藍眼白貓':
        message = TextSendMessage(text='米樂是一隻藍眼白貓')
        cat_image_url = 'https://i.imgur.com/vQDIpFI.jpg'

    elif message_text == '米多是一隻天花板上的灰虎斑貓':
        message = TextSendMessage(text='米多是一隻天花板上的灰虎斑貓')
        cat_image_url = 'https://i.imgur.com/unwMinz.jpg'

    elif message_text == 'MIGO是一隻天使白貓':
        message = TextSendMessage(text='MIGO是一隻天使白貓')
        cat_image_url = 'https://i.imgur.com/WeTpt0Y.png'

    elif message_text == 'HOYA是一隻好野貓':
        message = TextSendMessage(text='HOYA是一隻好野貓')
        cat_image_url = 'https://i.imgur.com/lItdIR7.jpg'

    elif message_text == 'FIRA是一隻玳瑁貓':
        message = TextSendMessage(text='FIRA是一隻玳瑁貓')
        cat_image_url = 'https://i.imgur.com/tvWlNgp.jpg'

    elif message_text == '胖妲是一隻賓士貓':
        message = TextSendMessage(text='胖妲是一隻賓士貓')
        cat_image_url = 'https://i.imgur.com/ZlfZFRf.jpg'

    else:
        cat_image_url = 'https://i.imgur.com/Uz9DjSf.png'
        message = TextSendMessage(text='抱歉，我們暫時沒有這隻貓咪的介紹。')

    if cat_image_url is not None:
        cat_image = ImageSendMessage(
            original_content_url=cat_image_url,
            preview_image_url=cat_image_url
        )
        line_bot_api.reply_message(
            event.reply_token,
            [message, cat_image]
        )
    else:
        line_bot_api.reply_message(event.reply_token, message)

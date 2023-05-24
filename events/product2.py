from line_bot_api import *

products2 = {
    1: {
        'category': '罐裝果乾「MIGO來去兜風檸檬乾」',
        'title': '「MIGO來去兜風檸檬乾」',
        'img_url_1': 'https://i.imgur.com/j02O83u.jpg',
        'img_url_2': 'https://i.imgur.com/x8Rto2e.jpg',
        'price': 185,
        'weight': 150,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433620/3825346/1'
    },
    2: {
        'category': '罐裝果乾「念念不忘情人果乾」',
        'title': '「念念不忘情人果乾」',
        'img_url_1': 'https://i.imgur.com/jPNPTNe.jpg',
        'img_url_2': 'https://i.imgur.com/Fr4hE3L.jpg',
        'price': 185,
        'weight': 150,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433620/3825346/1'
    },
    3: {
        'category': '罐裝果乾「偷偷墨墨加點梅情人果乾」',
        'title': '「偷偷墨墨加點梅情人果乾」',
        'img_url_1': 'https://i.imgur.com/j02O83u.jpg',
        'img_url_2': 'https://i.imgur.com/x8Rto2e.jpg',
        'price': 185,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433713/3825495/1'
    },
    4: {
        'category': '罐裝果乾「米麒麟紅心芭樂乾」',
        'title': '「米麒麟紅心芭樂乾」',
        'img_url_1': 'https://i.imgur.com/M48wMoy.jpg',
        'img_url_2': 'https://i.imgur.com/UCAfwbJ.jpg',
        'price': 185,
        'weight': 140,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433822/3825784/1'
    },
    5: {
        'category': '罐裝果乾「宅宅熱愛喜芭樂乾」',
        'title': '「宅宅熱愛喜芭樂乾」',
        'img_url_1': 'https://i.imgur.com/v7t0wcC.jpg',
        'img_url_2': 'https://i.imgur.com/8iq3FS8.jpg',
        'price': 170,
        'weight': 150,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433814/3825724/1'
    },
    6: {
        'category': '罐裝果乾「HOYA好野旺旺無糖鳳梨乾」',
        'title': '「HOYA好野旺旺無糖鳳梨乾」',
        'img_url_1': 'https://i.imgur.com/JZViGi9.jpg',
        'img_url_2': 'https://i.imgur.com/6DpH7UM.jpg',
        'price': 170,
        'weight': 150,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433802/3825693/1'
    },
    7: {
        'category': '罐裝果乾「FIRA太陽無糖鳳梨花」',
        'title': '「FIRA太陽無糖鳳梨花」',
        'img_url_1': 'https://i.imgur.com/9VqzQWQ.jpg',
        'img_url_2': 'https://i.imgur.com/WqmMXJk.jpg',
        'price': 185,
        'weight': 150,
        'post_url': 'https://langmiao13cat.waca.shop/cart/add/1433789/3825671/1'
    },
}


def product2_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='專屬貓奴的罐裝水果乾',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/Fl4V4Qv.jpg',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「MIGO來去兜風檸檬乾」',
                        data='action=product2&category=罐裝系列柑橘檬'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/VY7hzRW.jpg',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「米麒麟紅心芭樂乾」',
                        data='action=product2&category=罐裝系列米麒麟'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/86xost8.jpg',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「偷偷墨墨加點梅情人果乾」',
                        data='action=product2&category=罐裝系列情人果乾'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/lWXc02A.png',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「念念不忘情人果乾」',
                        data='action=product2&category=罐裝系列情人果乾'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/BP0N5G3.jpg',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「HOYA好野旺旺無糖鳳梨乾」',
                        data='action=product2&category=罐裝系列鳳梨乾'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/J74kYDf.jpg',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「宅宅熱愛喜芭樂乾」',
                        data='action=product2&category=罐裝系列鳳梨乾'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/wbSn4Yz.jpg',
                    action=PostbackAction(
                        label='貓奴的罐罐',
                        display_text='罐裝果乾「FIRA太陽無糖鳳梨花」',
                        data='action=product2&category=罐裝系列鳳梨乾'
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


def product2_event(event):
    bubbles = []

    for product_id in products2:
        if products2[product_id]:
            product2 = products2[product_id]
            bubble = {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": product2['img_url_1'],
                                            "size": "full",
                                            "aspectMode": "cover",
                                            "aspectRatio": "150:150",
                                            "gravity": "center"
                                        },
                                        {
                                            "type": "image",
                                            "url": product2['img_url_2'],
                                            "size": "full",
                                            "aspectMode": "cover",
                                            "aspectRatio": "150:150",
                                            "gravity": "center"
                                        }
                                    ],
                                    "flex": 1
                                }
                            ]
                        }
                    ],
                    "paddingAll": "0px"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "contents": [],
                                            "size": "xl",
                                            "wrap": True,
                                            "text": product2['title'],
                                            "color": "#CB9560",
                                            "align": "center",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": f"重量 {product2['weight']}g 價錢 ${product2['price']}",
                                            "color": "#CB9560",
                                            "size": "md",
                                            "align": "center"
                                        }
                                    ],
                                    "spacing": "xl"
                                }
                            ]
                        }
                    ],
                    "paddingAll": "20px",
                    "backgroundColor": "#ECECEC"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "添加到官方購物車",
                                "uri": product2['post_url']
                            },
                            "color": "#C88D52E8",
                            "style": "primary",
                            "height": "sm"
                        }
                    ],
                    "backgroundColor": "#ECECEC"
                }
            }

            bubbles.append(bubble)

    flex_message = FlexSendMessage(
        alt_text='人類的罐罐，密封易拉罐設計',
        contents={
            "type": "carousel",
            "contents": bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])

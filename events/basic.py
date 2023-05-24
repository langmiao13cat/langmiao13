from line_bot_api import *


def column_quick_reply_event(event):
    if event.message.text == '@關於浪喵果乾舖':
        message_text = TextSendMessage(text='喵喵喵以下是關於我們',
                                       quick_reply=QuickReply(items=[
                                           QuickReplyButton(
                                               action=MessageAction(
                                                   label="關於浪喵果乾的故事", text="貓奴講故事吧")),
                                           QuickReplyButton(
                                               action=URIAction(
                                                   label="Facebok粉絲團",
                                                   uri="https://www.facebook.com/langmiao13cat/")),
                                           QuickReplyButton(
                                               action=URIAction(
                                                   label="IG追蹤我們吧",
                                                   uri="https://www.instagram.com/langmiao13cat/")),
                                           QuickReplyButton(
                                               action=URIAction(
                                                   label="宣傳影片",
                                                   uri="https://www.youtube.com/watch?v=gym7_aGc7vc")),
                                           QuickReplyButton(
                                               action=MessageAction(
                                                   label="千萬別按",
                                                   text="好奇心會害死一隻貓唷！！，\n恭喜你獲得加入專屬會員，\n請手動輸入回應【加入會員】")),
                                           QuickReplyButton(
                                               action=MessageAction(
                                                   label="我是貓奴", text="恭喜您，以記錄成為資深貓奴")),
                                           QuickReplyButton(
                                               action=MessageAction(
                                                   label="有貓我就愛",
                                                   text="未來的你也會與你相遇的貓產生屬於你們的故事。"))
                                       ]))

        line_bot_api.reply_message(event.reply_token, message_text)


def about_us_event(event):
    text_message = event.message.text
    if text_message == '貓奴講故事吧':
        emoji = [
            {
                "index": 0,
                "productId": "5ac21184040ab15980c9b43a",
                "emojiId": "010"
            },
            {
                "index": 10,
                "productId": "5ac21184040ab15980c9b43a",
                "emojiId": "010"
            },
            {
                "index": 14,
                "productId": "5ac21b4f031a6752fb806d59",
                "emojiId": "074"
            },
            {
                "index": 17,
                "productId": "5ac21b4f031a6752fb806d59",
                "emojiId": "074"
            }
        ]

        about_us_message = TextSendMessage(text='''$ 【浪喵果乾舖】 $
貓奴$果乾$貓，
一個貓奴與流浪貓的果乾舖
在外流浪的浪浪們遇上
住在台南玉井的貓奴

與第13隻浪喵相遇的同時，
一次吃果乾時 一個的想法出現，
不如把果乾與貓的名子結合，
創造出獨一無二的果乾舖，
就這樣與貓的相遇故事
讓平凡無奇的果乾賦予新生命，

-台灣的在地水果
-低溫長時間烘焙
-純手工細心製作
-健康天然無添加
-充滿愛的水果乾

我們希望在一邊吃果乾的同時，
也能瞭解貓奴與貓相遇的故事。''', emojis=emoji)

        sticker_message = StickerSendMessage(
            package_id='6359',
            sticker_id='11069862'
        )

        about_us_img = 'https://i.imgur.com/cXVXaN0.png'

        image_message = ImageSendMessage(
            original_content_url=about_us_img,
            preview_image_url=about_us_img
        )

        line_bot_api.reply_message(
            event.reply_token,
            [about_us_message, sticker_message, image_message])


def store_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='來去逛逛浪喵果乾舖吧',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/DyM59h0.png',
                    action=URIAction(
                        label='浪喵果乾舖官網',
                        uri='https://langmiao13cat.waca.shop/'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/gvjuB0n.png',
                    action=URIAction(
                        label='浪喵果乾舖PINKO設計',
                        uri='https://www.pinkoi.com/store/langmiao13cat'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/wuHrNzw.png',
                    action=URIAction(
                        label='浪喵的LINE購物商城',
                        uri='https://ecmall.line.me/shops/@023jwouw'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, image_carousel_template_message)


def store3_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇想服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/yF2eLYc.png',
                    action=MessageAction(
                        label="【貓奴必吃】",
                        text="貓奴一定要吃天然水果乾",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/kNp7PTq.png',
                    action=MessageAction(
                        label="【貓奴的罐】",
                        text="專屬貓奴的罐裝水果乾",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/42KybXX.png',
                    action=MessageAction(
                        label="【必選禮盒】",
                        text="浪喵果乾禮盒系列"
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/nB4Uyh6.png',
                    action=MessageAction(
                        label="【文創小物】",
                        text="貓奴必備文創小物",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/yyavMEF.png',
                    action=MessageAction(
                        label="【貓奴私藏】",
                        text="貓奴私藏的精選美食",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/JeOr2do.png',
                    action=MessageAction(
                        label="【漿漾子喝】",
                        text="米麒麟·漿樣子喝果乾水",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/tSBhITm.png',
                    action=MessageAction(
                        label="【毛孩專區】",
                        text="米麒麟毛孩生活館",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/O9gOP61.png',
                    action=MessageAction(
                        label="【專屬客製】",
                        text="客製化專屬於您的故事",
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/P9sJ6xu.png',
                    action=MessageAction(
                        label="觀看更多的新生命訊息",
                        text="@浪喵賦予的新生命",
                    )
                ),
            ]
        )
    )

    line_bot_api.reply_message(
        event.reply_token,
        image_carousel_template_message
    )


def store2_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='來看最近貓奴在幹嘛',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/rrnK8Vj.png',
                    action=URIAction(
                        label='浪喵果乾舖官網',
                        uri='https://langmiao13cat.waca.shop/product/detail/1468447'
                    )
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, image_carousel_template_message)


def deallocating_event(event):
    message = TextSendMessage(
        text='最新優惠：任選２件８８折優惠！\n\n點擊以下連結查看詳細內容：\nhttps://langmiao13cat.waca.shop/onsale/2P88D/25220')

    deallocating_image_url = 'https://i.imgur.com/gKw2Xvu.png'
    cat_image = ImageSendMessage(
        original_content_url=deallocating_image_url,
        preview_image_url=deallocating_image_url
    )

    line_bot_api.reply_message(
        event.reply_token,
        [message, cat_image]
    )


def deallocating13_event(event):
    message = TextSendMessage(text='找貓奴~喵喵喵')
    line_bot_api.reply_message(event.reply_token, message)


def stop1_event(event):
    message = TextSendMessage(
        text='目前只接客製化果乾禮盒，想多瞭解請點選「@呼叫貓奴」功能。', )

    stop1_image_url = 'https://i.imgur.com/bBsZkPy.jpg'

    cat_image = ImageSendMessage(
        original_content_url=stop1_image_url,
        preview_image_url=stop1_image_url
    )

    line_bot_api.reply_message(
        event.reply_token,
        [message, cat_image]
    )


def stop2_event(event):
    message = TextSendMessage(
        text='貓奴設計的文創小物，\n貓奴為了主子們的罐罐，\n浪喵果乾舖貓奴設計的一些文創商品\n\n點擊以下連結查看詳細內容：\nhttps://langmiao13cat.waca.shop/category'
             '/95796')
    deallocating_image_url = 'https://i.imgur.com/tAIRcLC.jpg'

    cat_image = ImageSendMessage(
        original_content_url=deallocating_image_url,
        preview_image_url=deallocating_image_url
    )

    line_bot_api.reply_message(
        event.reply_token,
        [message, cat_image]
    )


def stop3_event(event):
    message = TextSendMessage(text='https://langmiao13cat.waca.shop/category/81973')
    line_bot_api.reply_message(event.reply_token, message)


def stop4_event(event):
    message = TextSendMessage(text='規劃中，請敬請期待')
    line_bot_api.reply_message(event.reply_token, message)


def stop5_event(event):
    message = TextSendMessage(text='來不及上架怎麼辦XD,https://langmiao13cat.waca.shop/category/108500')
    line_bot_api.reply_message(event.reply_token, message)


def stop6_event(event):
    message = TextSendMessage(
        text='貓奴設計的自有品牌設計，\n更多款式敬請期待，\nhttps://langmiao13cat.waca.shop/product/detail/1468447')
    line_bot_api.reply_message(event.reply_token, message)

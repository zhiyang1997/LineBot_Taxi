import requests
#app.py
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
# 需要額外載入對應的函示庫
from linebot.models import (ButtonsTemplate, MessageAction, MessageEvent,
                            MessageTemplateAction, PostbackAction,
                            TemplateSendMessage, TextMessage, TextSendMessage,
                            URIAction)

app = Flask(__name__)

line_bot_api = LineBotApi('ZxLhW51F0aLnqPEiAPQFZgm80HPCD7Nvo21GRpHtPayokgZIGV+t/ZsIWKtx6X6Y10eh/Qahmfcb/tgJ/ErzD5YpR/O8jrIqC1lFi7V7ffESsVt3avdCbgezicqTSZALpgTAFhs+qc6HnXXui5JGdQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7101b093a5e25db742fc69404f47fcdb')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    UserId = event.source.user_id
    profile = line_bot_api.get_profile(UserId)
    print(profile)
    #line_bot_api.reply_message(
    #     event.reply_token,[TextSendMessage(text = profile.display_name),TextSendMessage(text = profile.user_id)]
    #     )
    if event.message.text == "選擇身分":
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                title='身分確認',
                                text='請選擇您是司機或是乘客',
                                actions=[
                                    MessageTemplateAction(
                                        label = '司機',
                                        text = '司機'
                                    ),
                                    MessageTemplateAction(
                                        label='乘客',
                                        text = '乘客'
                                    )
                                ]
                            )
                        )
                    )
    if event.message.text == '司機':
        line_bot_api.reply_message(
            event.reply_token,[TextSendMessage(text = "需要您的一些基本資料，回覆格式如下。"),TextSendMessage(text = "姓名:XXX\n手機:09XXXXXXXX\n車牌號碼:XXX-XXX\n車子特徵:白色ALTIS\n車隊:A")]
            )
    if "車牌號碼" and "車子特徵" in event.message.text:
        driver = []
        web = requests.get('https://script.google.com/macros/s/AKfycbx0pSOgI9su4PuwYVolwtdfakpE7aooffBiH0CuIYWRevQ5UxXIYmDQixng8EJwqKlRXA/exec')
        # print(web.json()[-1][0])
        driver_id = web.json()[-1][0]
        last_driver_id = int(driver_id[1:])+1
        # print(driver_id[:-1] + str(last_driver_id))
        driver.append(driver_id[:-1] + str(last_driver_id))
        driver.append(profile.user_id)
        driver_data = event.message.text
        driver.append(driver_data.split( )[0][3:])
        driver.append(driver_data.split( )[1][3:])
        driver.append(driver_data.split( )[2][5:])
        driver.append(driver_data.split( )[3][5:])
        driver.append(driver_data.split( )[4][3:])
        print(driver)

        url = 'https://script.google.com/macros/s/AKfycbzSbrQR17YGyLcD-N60JqT3JIeN1QLfQ0rcbI78UAOov3xY7WU07-URgSTtpQULVxV9dA/exec'

        params = {
            'name':'driver',
            'data':'[' + '"' + driver[0] + '"' + "," + '"' + driver[1] + '"' +  "," + '"' + driver[2] + '"' + "," + '"' + driver[3] + '"' + "," + '"' + driver[4] + '"' + "," + '"' + driver[5] + '"' + "," + '"' + driver[6] + '"' + ']'
        }
        web = requests.get(url=url, params=params)

        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text = "感謝您的回覆，已幫你建檔完成，可以開始接單了！")
            )

    if event.message.text == "地圖叫車":
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text = "地圖叫車")
            )
    if event.message.text == "使用說明":
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text = "使用說明")
            )
    if event.message.text == "設定":
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text = "設定")
            )

if __name__ == "__main__":
    app.run()

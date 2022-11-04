#app.py
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

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
    print(profile.user_id)

    line_bot_api.reply_message(
        event.reply_token,[TextSendMessage(text = profile.display_name),TextSendMessage(text = profile.user_id)]
        )


if __name__ == "__main__":
    app.run()
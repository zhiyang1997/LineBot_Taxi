#Django modoule
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

#LINEbot Moudle
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *
#DriverServer
from .DriverServer import *
import time
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.


@csrf_exempt
def ChatBot(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:

            if isinstance(event, MessageEvent):

                ####司機端


                uid=event.source.user_id  #ID訊息
                if event.message.text  in ["我是司機"]:
                    message = IMDriver()
                    line_bot_api.reply_message(event.reply_token,message)
                if event.message.text  in ["上線接單"]: #車隊在資料庫內，而且uid身分是司機
                    message = takeOrder(uid)
                    line_bot_api.reply_message(event.reply_token,message)
                if event.message.text in ["A車隊","B車隊","C車隊"]: #車隊在資料庫內，而且uid身分是司機
                    message = TextSendMessage(text=f"您現在為「{event.message.text}」服務，正在為您尋找附近乘客…")
                    line_bot_api.reply_message(event.reply_token,message)
                    
                    #進行接單
                    line_bot_api.push_message(uid, waitOrder(uid))
                if event.message.text in ["確認接單"]: #車隊在資料庫內，而且uid身分是司機
                    
                    #進行接單ComfirmOrder(uid)
                    line_bot_api.push_message(uid, successOrder(uid))
                    time.sleep(10)
                    line_bot_api.push_message(uid, ComfirmOrder(uid))
                if event.message.text in ["是"]: #先判斷是不是訂單，如果沒有打是會出問題，所以會先偵測目前有無訂單
                    line_bot_api.push_message(uid, StartCalcular(uid))
                if event.message.text in ["開始跳表"]: #先判斷是不是訂單，如果沒有打是會出問題，所以會先偵測目前有無訂單
                    message = TextSendMessage(text=f"祝您旅途平安！\n目前里程數：0 KM\n費率小計：$ 80")
                    line_bot_api.push_message(uid, message)
                    time.sleep(30)
                    message = TextSendMessage(text=f"目前里程數：7.2 KM\n費率小計：$ 130")


                ####客戶端

                
                    

            

                
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
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
from .passengerServer import *

#Driver表單
from .forms import driverForm
from .models import *

import time
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


# Create your views here.
def driverlogin(request):
    form = driverForm()
    if request.method == 'POST':
        driver_id = request.POST['driver_id']
        phone_number = request.POST['phone_number']
        #判斷是否成功
        


    context = {
        'form':form
    }
    return render(request, 'comfirm/login.html', context)


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
                #使用說明
                if event.message.text in ["使用說明"]:
                    message = TextSendMessage(text=f"""請輸入您的手機號碼～\n***請勿加符號或空格***\n例：0900123456】""")
                    line_bot_api.reply_message(event.reply_token,message)
                if event.message.text in ["客服中心"]:
                    message = TextSendMessage(text="【24小時客服專線\n0900123456\n0901123456\n【其他服務\n*代駕/跑腿/代購/旅遊包車*\n請加LINE好友：http://line.com/xxx")
                    line_bot_api.reply_message(event.reply_token,message)

                if event.message.text  in ["我要叫車"]:
                    message = TextSendMessage(text=f"""請輸入您的手機號碼～\n***請勿加符號或空格***\n【例：0900123456】""")
                    line_bot_api.reply_message(event.reply_token,message)
                
                if event.message.text in ["確認叫車"]:
                    message = TextSendMessage(text=f"""收到！正在為你尋找附近司機…""")
                    line_bot_api.reply_message(event.reply_token,message)
        
                #if 有單子
                # message = TextSendMessage(text="""找到司機啦～

                # 您的司機正在路上，預計【10分鐘】後抵達！

                # 【車牌】MBY8302
                # 【車型】白TOYOTA YARIS

                # 請儘速前往上車地點～
                # """)
                # line_bot_api.push_message(uid, message)


                #已上車
                if event.message.text in ["已上車"]:
                    message = TextSendMessage(text=f"""司機已開始跳表計費，
                    祝您旅途平安～
                    目前里程數：0 KM
                    費率小計：$ 80""")
                    line_bot_api.reply_message(uid, message)

#
# message = TextSendMessage(text=f"""
# 即將抵達目的地！已自動停止跳表。
# """)

                    # message = TextSendMessage(text=f"""
                    # 訂單已完成！
                    # 總里程數：10.3KM
                    # 總金額：$ 245
                    # """)
                    # line_bot_api.reply_message(event.reply_token,message)
# """
# 感謝您選擇女神大車隊！
# 希望下次再為您服務～
# """    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
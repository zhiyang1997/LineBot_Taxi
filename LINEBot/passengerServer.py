import json
from linebot.models import *




'''
請輸入您的手機號碼～
***請勿加符號或空格***
【例：0900123456】
'''

#以乘客來講，可能以不用輸入的方式，而是用定位方式會比較方便
#keyword: google api 計程車
''' #可以改成定位服務API(uber)
請輸入上車地點（完整地址）j
【例：楠梓區卓越路2號】
'''

'''
請輸入下車地點（完整地址）
【例：楠梓區卓越路2號】
'''

'''
是否有其他備註？
如：地址備註、禁煙、不聊天
1.我要留言
    if true請輸入您給司機的備註～
2.暫時不用
'''

'''
確認叫車？
預估車程：17分鐘
預估車資：280元
確認叫車
請燒等
'''

'''
收到！正在為你尋找附近司機…
'''

'''
找到司機啦～

您的司機正在路上，預計【10分鐘】後抵達！

【車牌】MBY8302
【車型】白TOYOTA YARIS

請儘速前往上車地點～

'''

'''
司機已抵達！是否上車？
等待中
已上車
'''

''''
司機已開始跳表計費，
祝您旅途平安～
目前里程數：0 KM
費率小計：$ 80
'''

'''
目前里程數：7.2 KM
費率小計：$ 130
'''


def Waittaxi():
    format= {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "司機已抵達！是否上車？",
                "weight": "bold",
                "size": "xl"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "separator"
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "已上車",
                "text": "已上車"
                },
                "flex": 2
            },
            {
                "type": "button",
                "action": {
                "type": "message",
                "label": "等待中",
                "text": "等待中"
                },
                "flex": 2
            }
            ]
        }
        }
    flex_message = FlexSendMessage(
        alt_text="ComfirmOrder",
        contents=format
        
    )

    return flex_message






def callTaxi():
    format = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "確認叫車？",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "預估車程：",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 2
                            },
                            {
                                "type": "text",
                                "text": "17分鐘",
                                "wrap": True,
                                "color": "#666666",
                                "size": "sm",
                                "flex": 5
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "預估車資：",
                                "color": "#aaaaaa",
                                "size": "sm",
                                "flex": 2
                            },
                            {
                                "type": "text",
                                "text": "280元",
                                "wrap": True,
                                "color": "#666666",
                                "size": "sm",
                                "flex": 5
                            }
                            ]
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "確認叫車",
                        "text": "確認叫車"
                        },
                        "flex": 2
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "稍等一下",
                        "text": "稍等一下"
                        },
                        "flex": 2
                    }
                    ]
                }
                }
    
    flex_message = FlexSendMessage(
        alt_text="ComfirmOrder",
        contents=format
        
    )

    return flex_message


# def startcompular():
#     reutrn '''司機已開始跳表計費，
#     祝您旅途平安～
#     目前里程數：0 KM
#     費率小計：$ 80
#     '''
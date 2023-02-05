import json
from linebot.models import *


def StartCalcular(uid):
    format = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "開始跳表計費？",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "開始跳表",
          "text": "開始跳表"
        }
      }
    ],
    "flex": 0
  }
}
    
    flex_message = FlexSendMessage(
        alt_text="StartCalcular",
        contents=format
        
    )

    return flex_message    

def ComfirmOrder(uid):
    time = 10
    format = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "乘客是否上車？",
        "weight": "bold",
        "size": "xl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "是",
          "text": "是"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "否",
          "text": "否"
        }
      }
    ],
    "flex": 0
  }
}

    flex_message = FlexSendMessage(
        alt_text="ComfirmOrder",
        contents=format
        
    )

    return flex_message


def successOrder(uid):
    time = 10
    format = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "接單成功！ ",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "text",
                "text": "乘客已收到您的資訊～ "
            },
            {
                "type": "text",
                "text": f"預計{time}分鐘抵達上車地點…"
            }
            ]
        }
        }
    flex_message = FlexSendMessage(
        alt_text="success",
        contents=format
        
    )

    return flex_message

#得到定單資訊
def waitOrder(uid):

    #LIFF進去網頁取得GPS及uid，配對完成等到接單後關閉網頁，並主動推撥訂單資訊
    start = "我家" #取得訂單的起始位置
    end = "你家" #取得訂單的結束位置
    format = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "乘客叫車請求",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "text",
                "text": f"【上車】{start}"
            },
            {
                "type": "text",
                "text": f"【下車】{end}"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "horizontal",
            "spacing": "sm",
            "contents": [
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "確認接單",
                "text": "確認接單"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "略過",
                "text": "略過"
                }
            }
            ],
            "flex": 0
        }
        }
    flex_message = FlexSendMessage(
        alt_text="waitOrder",
        contents=format
        
    )

    return flex_message


def takeOrder(uid):
    #判斷uid有在資料庫內，若沒有回傳驗證失敗，有則判斷是否接單


    #判斷有沒有接單，若有就回傳偵測失敗

    #若沒有接單則回傳車隊選項

    format = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "成功上線！",
                "weight": "bold",
                "size": "xl"
            },
            {
                "type": "text",
                "text": "請選擇欲綁定的車隊代號："
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "A車隊",
                "text": "A車隊"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "B車隊",
                "text": "B車隊"
                }
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "margin": "sm"
            }
            ],
            "flex": 0
        }
        }
    flex_message = FlexSendMessage(
        alt_text="takeOrder",
        contents=format
        
    )

    return flex_message





def IMDriver():
    format = {
        "type": "bubble",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "weight": "bold",
                "size": "xl",
                "text": "我是司機",
                "contents": []
            },
            {
                "type": "text",
                "text": "司機專屬功能！非司機請移步喔～"
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "上線接單",
                "text": "上線接單"
                }
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type": "message",
                "label": "司機驗證",
                "text": "司機驗證"
                }
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "margin": "sm"
            }
            ],
            "flex": 0
        }
        }

    flex_message = FlexSendMessage(
        alt_text="I'm a Driver",
        contents=format
        
    )

    
    return flex_message

    
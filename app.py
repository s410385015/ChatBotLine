from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('NfKPy0NS79K6hAdfB/9rm11oq2kTugvZKgzkpLtBoo1aNgcHxbt4kEYGrC8Cph/kpYDqK9EDPvpzx3Q0L2zwzTZ9Uid3qDKbQ/O3dN8R6lMwqIFhvnPJTRlsXO29p2wr/ZNNqM+vxaxvdq8TJgTGQwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('56d0c48f38150bf68500dde827e5791b')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    message = TextSendMessage(text='我不是機器人')
    line_bot_api.reply_message(event.reply_token, message)
    message = TextSendMessage(text='我是真人，是大大肚肚')
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

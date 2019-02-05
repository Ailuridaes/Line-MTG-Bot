import boto3
import botocore
import logging
import json
import datetime
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# config
with open('./config.json', 'r') as file:
    config = json.loads(file.read())

# content_db_user = config['content-db-username']
line_bot_api = LineBotApi(config['channel-access-token'])
handler = WebhookHandler(config['channel-secret'])

def lambda_handler(event, context):
    
    # log event
    logger.info(event)

    # get X-Line-Signature header value
    signature = event['headers']['X-Line-Signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return 400

    return 200


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))
    except LineBotApiError as e:
        logger.error(e.status_code)
        logger.error(e.error.message)
        logger.error(e.error.details)

@handler.default()
def default(event):
    pass
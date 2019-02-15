import boto3
import botocore
import logging
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)
import mtg_api
from api_errors import GetCardError

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
    content = event.message.text
    end = len(content)

    # Determine if message has request(s) for MTG Bot
    start = content.find("[[") + 2
    requests = []
    while start > 1:
        end = content.find("]]", start)
        request = content[start:end]
        logger.info("Request: " + request)
        if len(request) > 2:
            requests.append(request)
        start = content.find("[[", end) + 2

    # Generate response messages for requests
    messages = [get_message_for_request(r) for r in requests]

    # Send response(s)
    if len(messages) > 0:
        try:
            line_bot_api.reply_message(
                event.reply_token,
                messages)
        except LineBotApiError as e:
            logger.error(e.status_code)
            logger.error(e.error.message)
            logger.error(e.error.details)

@handler.default()
def default(event):
    pass

def get_message_for_request(request):
    request_parts = request.split('|')
    try:
        if(request[0] == '?'):
    
            # Get card rulings
            card = mtg_api.get_card(request_parts[0][1:])
            rulings = mtg_api.get_card_ruling(card)
            if(len(rulings) > 0):
                # construct rulings message
                message_text = f'Rulings for "{card.name}":'
                for ruling in rulings:
                    message_text += f'\n{ruling.date} by {ruling.source} - {ruling.text}'
                return TextMessage(text=message_text)
            else:
                return TextSendMessage(text=f'No rulings were found for "{card.name}".')
        else:
    
            # Get card image
            card = mtg_api.get_card(request_parts[0], request_parts[1] if len(request_parts) > 1 else '')
            return ImageSendMessage(card.image_uri, card.image_uri)
    except GetCardError as e:
        return TextSendMessage(text=e.message)

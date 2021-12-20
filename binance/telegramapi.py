
import telegram_send

def assert_user(message :str):
    telegram_send.send(messages=[message])
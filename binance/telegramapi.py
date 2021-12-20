# There are problems and there is C programming language
#                                   Muzaffer Irmak YAVUZ



import telegram_send

def assert_user(message :str):
    telegram_send.send(messages=[message])
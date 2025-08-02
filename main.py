from bot import get_updates
from handlers import handler_message
import time


def main():
    print("Bot ishga tushdi")
    offset = None
    while True:
        updates = get_updates(offset)
        if 'result' in updates:
            for update in updates['result']:
                offset = update['update_id'] + 1
                message = update.get('message')
                if message:
                    chat_id = message['chat']['id']
                    text = message.get('text', '')
                    handler_message(text, chat_id)
                else:
                    print("Message mavjud emas:", update)

if __name__ == '__main__':
    main()


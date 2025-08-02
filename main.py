from handlers import handler_message
from telegram_api import get_updates  
import time

def main():
    print("Bot ishga tushdi")
    offset = None
    while True:
        updates = get_updates(offset)
        if 'result' in updates:
            for update in updates['result']:
                offset = update['update_id'] + 1
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    text = update['message'].get('text', '')
                    handler_message(text, chat_id)
        time.sleep(1)

if __name__ == '__main__':
    main()

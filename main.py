import time

from VK import AccountVk
from config import access_token,ID, words_for_search


def main():
    account = AccountVk(access_token)
    account.send_message_to_id(ID,"Работыает...")
    words = words_for_search
    while True:
        message = account.get_latest_message()
        if message:
            print(message)
            wm = account.filter(words,message)
            if wm:
                account.send_message_to_id(ID,"чекни беседу")
                account.send_message_to_id(ID,f"{message}")
        time.sleep(2)

if __name__ == "__main__":
    main()
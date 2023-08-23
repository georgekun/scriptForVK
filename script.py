import vk_api
from config import access_token,ID, words_for_search

"""Получение ACCESS происходило не через основной вк апи, а через сторонний сервис.
Поэтому есть смысл использовать не настойщий аккаунт"""
class AccountVk():
    last_id = -555555
    def __init__(self):
        self.session = vk_api.VkApi(token=access_token)
        self.vk= self.session.get_api()

    def get_latest_message(self,chat_id = 0):
        """Метод возвращает последние сообщение чата. Индекс ["items"][0] указывает на самый первый чат в списке. 
        поэтому стоит закрепить чат, который требуется слушать """
        group = self.session.method(
            "messages.getConversations",
            {})
        
        id = group["items"][chat_id]["last_message"]["id"]
        if id != self.last_id:
          last_message = group["items"][chat_id]["last_message"]["text"]
          self.last_id = id
          return last_message
          
      
    def filter(self,words:list,text:str):
        #Проверка на наличие слов в тексте сообщения
        for word in words:
          if word in text:
              return True
          else:
              continue

    def send_message_to_id(self,users_id:list,text):
        for user in users_id:
            self.session.method("messages.send",{"user_id":user,"random_id":"0","message":text})


def main():
    print("Начало работы...")
    account = AccountVk()
    while True:
        words = words_for_search
        message = account.get_latest_message() 
        if message:
          wm = account.filter(words,message)
          if wm:
                account.send_message_to_id(ID,"чекни беседу")
                account.send_message_to_id(ID,f"{message}")

  
if __name__ == "__main__":
    main()
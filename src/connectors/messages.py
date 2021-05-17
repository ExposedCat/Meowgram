from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio


class MessagesManager:

    loaded_chat_id = []
    loaded_messages = []

    def send_message(self, chat, text):
        request = aio.run(client.send_message, (chat, text))
        return request.result()

    def show_messages(self, window, chat_id):
        print(chat_id)

        if chat_id not in self.loaded_chat_id:
            request = aio.run(client.get_messages, (chat_id,))
            messages = request.result()

            self.loaded_chat_id.append(chat_id)
            self.loaded_messages.append(messages)

        else:
            index = self.loaded_chat_id.index(chat_id)
            messages = self.loaded_messages[index]

        window.update_messages_listbox(messages)


messages_manager = MessagesManager()

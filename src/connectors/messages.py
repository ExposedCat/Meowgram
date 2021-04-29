from meowgram.widgets.message_row import MessageRow

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import async_run


class MessagesManager:
    def show_messages(self, window, chat_id):
        print(chat_id)
        request = async_run(client.get_messages, (chat_id,))
        messages = request.result()
        current_messages = window.message_box.get_children()
        for message in current_messages:
            window.message_box.remove(message)
        for message in reversed(messages):
            window.message_box.add(MessageRow(message))


messages_manager = MessagesManager()

from meowgram.widgets.message_row import MessageRow

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import async_run


class MessagesManager:

    loaded_chat_id = []
    loaded_messages = []

    def show_messages(self, window, chat_id):
        print(chat_id)

        actual_chat_id = self._get_actual_id(chat_id)

        if actual_chat_id not in self.loaded_chat_id:
            request = async_run(client.get_messages, (chat_id,))
            messages = request.result()

            self.loaded_chat_id.append(actual_chat_id)
            self.loaded_messages.append(messages)

        else:
            index = self.loaded_chat_id.index(actual_chat_id)
            messages = self.loaded_messages[index]

        self.update_window_message_box(messages, window)

    def update_window_message_box(self, messages, window):
        current_messages = window.message_box.get_children()
        for message in current_messages:
            window.message_box.remove(message)

        for message in reversed(messages):
            window.message_box.insert(MessageRow(message), -1)

    def _get_actual_id(self, chat_id):
        if hasattr(chat_id, 'channel_id'):
            actual_id = chat_id.channel_id
        else:
            actual_id = chat_id.user_id
        return actual_id

messages_manager = MessagesManager()

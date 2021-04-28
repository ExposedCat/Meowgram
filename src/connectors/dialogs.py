from meowgram.widgets.contact_row import ContactRow
from meowgram.widgets.message_row import MessageRow

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import async_run


class DialogsManager:
    def show_dialogs(self, window):
        request = async_run(client.get_dialogs, ())
        dialogs = request.result()
        for dialog in dialogs:
            window.contacts_listbox.insert(ContactRow(dialog), -1)


dialogs_manager = DialogsManager()

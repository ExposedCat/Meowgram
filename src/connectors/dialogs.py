from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio


class DialogsManager:
    def show_dialogs(self, window):
        request = aio.run(client.get_dialogs, ())
        dialogs = request.result()

        window.update_contacts_listbox(dialogs)


dialogs_manager = DialogsManager()

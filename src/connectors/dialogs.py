from meowgram.widgets.contact_row import ContactRow
from meowgram.widgets.message_row import MessageRow

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import async_run


class DialogsManager:
    def show_dialogs(self, window):
        request = async_run(client.get_dialogs, ())
        dialogs = request.result()
        print(dialogs.__dict__)
        for dialog in dialogs:
            print(dialog.message.__dict__)
            print(dialog.entity.__dict__)
            print(dialog.message.peer_id.__dict__)
            print(dialog.draft.__dict__)
            print(dialog.input_entity.__dict__)
            print(dialog.dialog.__dict__)
            print(dialog.dialog.notify_settings.__dict__)
            window.contacts_listbox.insert(ContactRow(dialog), -1)
            window.message_box.add(MessageRow(dialog))


dialogs_manager = DialogsManager()


from gi.repository import GObject, Gio

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio


class Dialog(GObject.GObject):
    __gtype_name__ = 'Dialog'

    name = GObject.Property(type=str, default='')
    last_message = GObject.Property(type=str, default='')

    def __init__(self, tl_dialog):
        super().__init__()
        self.dialog = tl_dialog

        self.name = tl_dialog.name




class DialogsManager:

    def __init__(self):
        self.dialog_model = Gio.ListStore.new(Dialog)

    def show_dialogs(self, window):
        request = aio.run(client.get_dialogs, ())
        tl_dialogs = request.result()

        for tl_dialog in tl_dialogs:
            dialog = Dialog(tl_dialog)
            self.dialog_model.append(dialog)


dialogs_manager = DialogsManager()

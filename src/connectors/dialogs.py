
from gi.repository import GObject, Gio, GLib

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio


class Dialog(GObject.GObject):
    __gtype_name__ = 'Dialog'

    name = GObject.Property(type=str, default='')
    last_message = GObject.Property(type=object)
    last_message_date = GObject.Property(type=object)
    muted_until = GObject.Property(type=object)

    is_user = GObject.Property(type=bool, default=False)

    _chat_id = None

    def __init__(self, tl_dialog):
        super().__init__()
        self.dialog = tl_dialog
        self.chat_id = tl_dialog.message.peer_id

        self.name = tl_dialog.name
        self.last_message = tl_dialog.message
        self.last_message_date = tl_dialog.message.date
        self.muted_until = tl_dialog.dialog.notify_settings.mute_until

        self.is_user = self.dialog.is_user

    @GObject.Property(type=object, default=_chat_id)
    def chat_id(self):
        chat_id_dict = self._chat_id.__dict__.values()
        chat_id = tuple(chat_id_dict)[0]
        return chat_id

    @chat_id.setter  # type: ignore
    def chat_id(self, chat_id):
        self._chat_id = chat_id


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

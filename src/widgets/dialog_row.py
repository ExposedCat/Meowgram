# dialog_row.py
#
# Copyright 2021 SeaDve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
from telethon.tl.types import UserStatusOffline, UserStatusRecently, UserStatusOnline

from meowgram.utils.fuzzify import Fuzzify
from meowgram.constants import Constants

# TODO show dialog picture
# TODO add indicator if a message was read
# TODO In get last active, fix unknown time
# TODO Don't just show "Photo" if it is actually a time


@Gtk.Template(resource_path=f"{Constants.PATHID}/ui/dialog_row.ui")
class DialogRow(Gtk.Box):
    __gtype_name__ = 'DialogRow'

    avatar = Gtk.Template.Child()

    dialog_name_label = Gtk.Template.Child()
    last_message_label = Gtk.Template.Child()
    message_sender_label = Gtk.Template.Child()
    time_label = Gtk.Template.Child()

    online_status = Gtk.Template.Child()
    mute_status = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    mention_status = Gtk.Template.Child()
    unread_label = Gtk.Template.Child()
    pin_status = Gtk.Template.Child()

    def __init__(self, dialog):
        super().__init__()

        self.dialog_name_label.bind_property('label', self.avatar, 'text')
        self.update(dialog)

    def update(self, dialog):
        self.dialog = dialog
        self.chat_id = self.dialog.message.peer_id

        self.dialog_name = getattr(self.dialog, 'title', self.dialog.name)
        self.last_message = self.dialog.message
        self.last_message_date = self.dialog.message.date
        self.muted_until = self.dialog.dialog.notify_settings.mute_until
        self.unread_mentions_count = self.dialog.unread_mentions_count
        self.unread_count = self.dialog.unread_count
        self.is_pinned = self.dialog.pinned
        self.is_from_self = self.dialog.message.out
        self.is_user = self.dialog.is_user
        self.is_online = self.get_is_online()

        self.set_dialog_name(self.dialog_name)
        self.set_last_message(self.last_message, self.is_user)
        self.set_last_message_date(self.last_message_date)

        self.set_message_status(self.is_from_self)
        self.set_dialog_status(self.unread_mentions_count, self.unread_count, self.is_pinned)
        self.set_mute_status(self.muted_until)
        self.set_online_status(self.is_online)

    def set_dialog_name(self, dialog_name):
        """Sets the dialog name of the dialog

        Parameter:
        dialog_name (str): The title of the dialog
        """

        self.dialog_name_label.set_text(dialog_name)

    def set_last_message(self, last_message, is_user):
        """Sets the last message of the dialog

        Parameters:
        last_message (tl.patched.Message): The last message from the dialog
        is_user (bool): If the dialog is a user
        """

        if last_message.out:
            sender_name = "You"
        elif is_user:
            sender_name = ""
        else:
            sender_name = getattr(
                last_message.sender, 'post_author', getattr(last_message.sender, 'first_name', "")
            )

        if last_message.message:
            message_text = last_message.message.replace("\n", " ")
        elif action := last_message.action:
            message_text = f"{sender_name} did something - {action}"
            sender_name = ""
        elif last_message.media:
            message_text = "🖼️ Photo"

        self.last_message_label.set_text(message_text)
        self.message_sender_label.set_text(f"{sender_name}{': ' if sender_name else ''}")

    def set_last_message_date(self, time):
        """Sets the time sent of the last message

        Parameter:
        time (datetime.datetime): The last message from the dialog
        """

        fuzzified_time = Fuzzify.dialog_last_message(time)
        self.time_label.set_text(fuzzified_time)

    def set_dialog_status(self, unread_mentions_count, unread_count, is_pinned):
        """Sets the status of the dialog

        Parameters:
        unread_mentions_count (int): The number of unread mentioned messages
        unread_count (int): The number of messages unread in the dialog
        is_pinned (bool): Whether the dialog is pinned
        """

        self.mention_status.set_visible(unread_mentions_count)
        self.unread_label.set_visible(unread_count > 1)
        self.unread_label.set_label(str(unread_count))
        self.pin_status.set_visible(is_pinned and not(unread_mentions_count or unread_count))

    def set_message_status(self, is_from_self):
        """Sets the status of your message sent to that dialog

        Parameter:
        is_from_self (bool): Whether the dialog is from self
        """

        self.read_status.set_visible(is_from_self)

    def set_mute_status(self, muted_until):
        """Sets the mute status of the dialog

        Parameter:
        muted_until (datetime.datetime): The date when the dialog will be unmuted
        """

        unread_label_style_context = self.unread_label.get_style_context()
        if muted_until:
            unread_label_style_context.add_class('muted-badge')
        else:
            unread_label_style_context.remove_class('muted-badge')
        self.mute_status.set_visible(muted_until)

    def set_online_status(self, is_online):
        """Sets the online status of the dialog

        Parameter:
        is_online (bool): Whether the dialog is online
        """

        self.online_status.set_visible(is_online)

    def get_last_active(self):
        """Returns the time when the dialog is last active

        Returns:
        str: The time when the dialog is last active
        """

        dialog_status = self.dialog.entity.status
        if isinstance(dialog_status, UserStatusOnline):
            last_active = "online"
        elif isinstance(dialog_status, UserStatusOffline):
            last_active = Fuzzify.dialog_last_active(dialog_status.was_online)
        elif isinstance(dialog_status, UserStatusRecently):
            last_active = "last seen recently"
        else:
            last_active = "Unknown time"

        return last_active

    def get_room_members_count(self):
        """Returns the number of members in a dialog

        Returns:
        str: The "{number} members" in the dialog
        """

        try:
            return f"{self.dialog.entity.participants_count} members"
        except AttributeError:
            return ""

    def get_is_bot(self):
        """Returns if the dialog is a bot

        Returns:
        bool: If the dialog is a bot
        """

        try:
            return self.dialog.entity.bot
        except AttributeError:
            return False

    def get_is_online(self):
        """Returns if the dialog is online

        Returns:
        bool: If the dialog is online
        """

        try:
            return isinstance(self.dialog.entity.status, UserStatusOnline)
        except AttributeError:
            return False

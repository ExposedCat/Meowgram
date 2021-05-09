# contactrow.py
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

import datetime

from gi.repository import Gtk
from telethon.tl.types import UserStatusOffline, UserStatusRecently, UserStatusOnline

from meowgram.utils.fuzzify import Fuzzify
from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/contactrow.ui")
class ContactRow(Gtk.Box):
    __gtype_name__ = 'ContactRow'

    chat_id = None
    avatar = Gtk.Template.Child()

    contact_name_label = Gtk.Template.Child()
    last_message_label = Gtk.Template.Child()
    time_label = Gtk.Template.Child()

    unread_label = Gtk.Template.Child()
    mention_status = Gtk.Template.Child()
    pin_status = Gtk.Template.Child()
    mute_status = Gtk.Template.Child()
    read_status = Gtk.Template.Child()
    online_status = Gtk.Template.Child()

    def __init__(self, dialog_data, **kwargs):
        super().__init__(**kwargs)

        self.contact_name_label.bind_property('label', self.avatar, 'text')
        self.update(dialog_data)

        # TODO show contact picture
        # TODO add indicator if a message was read

    def update(self, dialog_data):
        self.dialog_data = dialog_data
        self.chat_id = self.dialog_data.message.peer_id

        self.set_message_status()
        self.set_unread_status()
        self.set_mute_status()
        self.set_online_status()

        self.contact_name_label.set_text(self.get_contact_name())
        self.last_message_label.set_text(self.get_last_message())
        self.time_label.set_label(self.get_last_message_time())

    def get_contact_name(self):
        contact_name = getattr(self.dialog_data, 'title', self.dialog_data.name)
        return contact_name

    def get_last_message(self):
        message = self.dialog_data.message

        if message.out:
            sender_name = "You"
        elif self.dialog_data.is_user:
            sender_name = ""
        else:
            sender_name = getattr(
                message.sender, 'post_author', getattr(message.sender, 'first_name', "")
            )

        if message.message:
            last_message = message.message.replace("\n", " ")
        elif message.action:
            last_message = f"{sender_name} did something - {message.action}"
            sender_name = ""
        elif message.media:
            last_message = "🖼️ Photo"

        return f"{sender_name}{': ' if sender_name else ''}{last_message}"

    def get_last_message_time(self):
        return Fuzzify.dialog_last_message(self.dialog_data.message.date)

    def get_last_active(self):
        contact_status = self.dialog_data.entity.status
        if isinstance(contact_status, UserStatusOnline):
            last_active = "online"
        elif isinstance(contact_status, UserStatusOffline):
            last_active = Fuzzify.dialog_last_active(contact_status)
        elif isinstance(contact_status, UserStatusRecently):
            last_active = "last seen recently"
        else:
            # TODO replace with something from UserStatus
            last_active = "Unknown time"

        return last_active

    def get_room_members_count(self):
        try:
            return f"{self.dialog_data.entity.participants_count} members"
        except AttributeError:
            return ""

    def get_is_bot(self):
        try:
            return self.dialog_data.entity.bot
        except AttributeError:
            return False

    def set_unread_status(self):
        if self.dialog_data.unread_mentions_count:
            self.mention_status.set_visible(True)
        elif unread_count := self.dialog_data.unread_count:
            self.unread_label.set_visible(True)
            self.unread_label.set_label(str(unread_count))
        elif self.dialog_data.pinned:
            self.pin_status.set_visible(True)

    def set_message_status(self):
        self.read_status.set_visible(self.dialog_data.message.out)

    def set_mute_status(self):
        if self.dialog_data.dialog.notify_settings.mute_until:
            self.mute_status.set_visible(True)
            self.unread_label.get_style_context().add_class('muted-badge')

    def set_online_status(self):
        try:
            is_online = isinstance(self.dialog_data.entity.status, UserStatusOnline)
            self.online_status.set_visible(is_online)
        except AttributeError:
            pass

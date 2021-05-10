# message_row.py
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

from meowgram.utils.fuzzify import Fuzzify
from meowgram.constants import Constants

# TODO Fix selection theming in messages listbox
# TODO also, hide the sender_label when it is the same as in the headerbar
# TODO add proper read status
# TODO move avatar to most bottom part of message group
# TODO Implement message forward


@Gtk.Template(resource_path=f"{Constants.PATHID}/ui/message_row.ui")
class MessageRow(Gtk.Box):
    __gtype_name__ = 'MessageRow'

    avatar = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    time_label = Gtk.Template.Child()
    sender_label = Gtk.Template.Child()
    message_label = Gtk.Template.Child()
    reply_label = Gtk.Template.Child()

    message_bubble = Gtk.Template.Child()

    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)

        self.sender_label.bind_property('label', self.avatar, 'text')
        self.update(message)

    def update(self, message):
        self.message = message
        self.message_text = self.message.message

        if self.message.action:
            self.set_as_action_message()
        elif self.message.out:
            self.set_message_out()
            self.set_is_read(True)
        else:
            self.set_message_in()

        self.set_message_text(self.message_text)

        self.sender_label.set_label(self.get_message_sender())
        self.time_label.set_label(self.get_message_time())

        self.set_reply_message()
        self.set_forward_message()

    def set_message_text(self, message_text):
        """Sets the visible message

        Parameters:
        message_text (str): The last message from the dialog
        """

        if message_text:
            pass
        elif self.message.action:
            message_text = f"{self.get_message_sender()} did something - {self.message.action}"
        else:
            message_text = "<span style=\"italic\">Message type is not supported yet.</span>"
            self.message_label.set_use_markup("True")

        self.message_label.set_label(message_text)

    def get_message_time(self):
        return Fuzzify.message_time_sent(self.message.date)

    def get_message_sender(self):
        message_sender = self.message.sender
        try:
            contact_name = (f"{getattr(message_sender, 'first_name')} "
                            f"{str(message_sender.last_name or '')}")
        except AttributeError:
            contact_name = getattr(message_sender, 'title')
        return contact_name

    def set_reply_message(self):
        if self.message.reply_to:
            self.reply_label.set_visible(True)
            self.reply_label.set_label(f"The message has id of {self.message.reply_to_msg_id}")

    def set_forward_message(self):
        if fwd_from := self.message.fwd_from:
            print(fwd_from)

    def set_message_out(self):
        self.sender_label.set_visible(False)
        self.avatar.set_visible(False)
        self.set_halign(Gtk.Align.END)
        self.message_bubble.get_style_context().add_class('message-out')

    def set_message_in(self):
        self.sender_label.set_visible(True)
        self.avatar.set_visible(True)
        self.set_halign(Gtk.Align.START)
        self.message_bubble.get_style_context().add_class('message-in')

    def set_as_action_message(self):
        self.sender_label.set_visible(False)
        self.avatar.set_visible(False)
        self.time_label.set_visible(False)
        self.set_halign(Gtk.Align.CENTER)
        self.message_label.set_justify(Gtk.Justification.CENTER)
        self.message_bubble.get_style_context().add_class('message-action')

    def set_as_group(self, is_group):
        if is_group:
            self.sender_label.set_visible(False)
            self.avatar.set_visible(False)
            self.set_margin_start(38)

    def set_is_read(self, is_read):
        self.read_status.set_visible(True)
        if is_read:
            self.read_status.set_from_icon_name("message-out-read-symbolic")
        else:
            self.read_status.set_from_icon_name("message-out-unread-symbolic")

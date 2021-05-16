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

import bleach
from gi.repository import Gtk

from meowgram.utils.fuzzify import Fuzzify
from meowgram.constants import Constants

# TODO Fix selection theming in messages listbox
# TODO also, hide the sender_label when it is the same as in the headerbar
# TODO add proper read status
# TODO move avatar to most bottom part of message group
# TODO Implement fwd_from


@Gtk.Template(resource_path=f'{Constants.PATHID}/ui/message_row.ui')
class MessageRow(Gtk.Box):
    __gtype_name__ = 'MessageRow'

    avatar = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    time_label = Gtk.Template.Child()
    sender_label = Gtk.Template.Child()
    message_label = Gtk.Template.Child()
    reply_label = Gtk.Template.Child()

    message_bubble = Gtk.Template.Child()

    def __init__(self, message):
        super().__init__()

        self.update(message)

    def update(self, message):
        self.message = message
        self.message_text = self.message.message
        self.date_sent = self.message.date
        self.sender = self.message.sender
        self.reply_message = self.message.reply_to
        self.fwd_from = self.message.fwd_from
        self.is_out = self.message.out
        self.action = self.message.action

        self.set_message_text(self.message_text)
        self.set_date_sent(self.date_sent)
        self.set_message_sender(self.sender)

        self.set_reply_message(self.reply_message)
        self.set_fwd_from(self.fwd_from)

        if self.action:
            self.set_action(True)
        else:
            self.set_out(self.is_out)
            self.set_read(self.is_out)

    def _convert_user_to_str(self, user):
        """Converts a user object to a string

        Parameter:
        user (tl.types.User): The user object who sent the message

        Returns:
        str: The full name of user in string
        """

        try:
            user_fullname = (f"{user.first_name} {user.last_name or ''}")
        except AttributeError:
            user_fullname = user.title
        return user_fullname

    def set_message_text(self, message_text):
        """Sets the visible message

        Parameters:
        message_text (str): The last message from the dialog
        """

        if message_text:
            message_text = bleach.linkify(message_text, parse_email=True, callbacks=None)

        elif self.message.action:
            message_text = (f"{self._convert_user_to_str(self.sender)} "
                            f"did something - {self.message.action}")
        else:
            message_text = "<span style=\"italic\">Message type is not supported yet.</span>"

        self.message_label.set_label(message_text)

    def set_message_sender(self, sender):
        """Sets the sender of the message

        Parameter:
        sender (tl.types.User): The user who sent the message
        """

        stringified_sender = self._convert_user_to_str(sender)
        self.sender_label.set_label(stringified_sender)

    def set_date_sent(self, date):
        """Sets the time sent of the message

        Parameter:
        date (datetime.datetime): The time the message was sent
        """

        fuzzified_date = Fuzzify.message_time_sent(date)
        self.time_label.set_label(fuzzified_date)

    def set_read(self, is_read):
        """Shows if the message is already read by other

        Parameter:
        is_read (bool): If your message is already read by other
        """

        self.read_status.set_visible(self.is_out)
        icon_name = 'read' if is_read else 'unread'
        self.read_status.set_from_icon_name(f'message-out-{icon_name}-symbolic')

    def set_reply_message(self, reply_message):
        """Shows or hide the message in which self is replied to

        Parameter:
        is_read (tl.types.MessageReplyHeader): The message in which it is replied to
        """

        self.reply_label.set_visible(reply_message)
        if reply_message:
            self.reply_label.set_label(f"The message has id of {reply_message.reply_to_msg_id}")

    def set_fwd_from(self, fwd_from):
        """Shows the sender of the forwarded message

        Parameter:
        is_read (tl.types.MessageFwdHeader): The message object where the message is from
        """

        if fwd_from:
            print(fwd_from)

    def set_out(self, is_out):
        """Styles the message if it is from you or other

        Parameter:
        is_out (bool): Whether the message is from you
        """

        if is_out:
            self.set_halign(Gtk.Align.END)
            self.message_bubble.get_style_context().add_class('message-out')
        else:
            self.set_halign(Gtk.Align.START)
            self.message_bubble.get_style_context().add_class('message-in')

    def set_action(self, is_action):
        """Styles the message if it shows an action

        Parameter:
        is_action (bool): If the message is an action
        """

        self.time_label.set_visible(not is_action)
        self.set_halign(Gtk.Align.CENTER)
        self.message_label.set_justify(Gtk.Justification.CENTER)
        self.message_bubble.get_style_context().add_class('message-action')

    def set_grouping(self, is_first, is_last):
        """Styles the message if it is first or last in a group. This needs to be setup
        after set_grouping as it needs action and is_out property.

        Parameter:
        is_first (bool): If the message is first in a group
        is_last (bool): If the message is last in a group
        """

        neither_out_nor_action = not (self.is_out or self.action)
        self.sender_label.set_visible(is_first and neither_out_nor_action)
        self.avatar.set_visible(is_last and neither_out_nor_action)
        if not is_last:
            self.set_margin_start(38)
        else:
            self.set_margin_start(0)

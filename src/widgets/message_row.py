# messagerow.py
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

from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/messagerow.ui")
class MessageRow(Gtk.Grid):
    __gtype_name__ = 'MessageRow'

    status_box = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    time_label = Gtk.Template.Child()
    sender_label = Gtk.Template.Child()

    avatar = Gtk.Template.Child()
    message_label = Gtk.Template.Child()

    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)

        self.sender_label.bind_property('label', self.avatar, 'text')
        self.update(message)

        # TODO automatically hide the sender_label and reduce padding when
        # the sender is the same as the last one

        # TODO also, hide the sender_label when it is the same as in the headerbar

    def update(self, message):
        self.message = message

        if self.message.out:
            self.set_message_out()
        else:
            self.set_message_in()

        self.message_label.set_label(self.get_message())
        self.sender_label.set_label(self.get_message_sender())
        self.time_label.set_label(self.get_message_time())

    def get_message(self):
        if not (message := self.message.message):
            message = "<span style=\"italic\">Message type is not supported yet.</span>"
            self.message_label.set_use_markup("True")
        return message

    def get_message_time(self):
        last_message_time = self.message.date \
            .replace(tzinfo=datetime.timezone.utc) \
            .astimezone()

        today = datetime.datetime.now().astimezone()
        days_difference = (today - last_message_time).days

        if days_difference < 1:
            # TODO Make this work with military time
            format_string = '%I∶%M %p'  # 08:57 AM
        elif 1 <= days_difference < 7:
            format_string = '%a at %I∶%M %p'  # Fri at 08:57 AM
        elif days_difference >= 7:
            format_string = '%b %d at %I∶%M %p'  # Apr 08 at 08:57 AM
        return last_message_time.strftime(format_string)

    def get_message_sender(self):
        if not (message_sender := self.message.sender.username):
            message_sender = ""
        return message_sender

    def set_message_out(self):
        self.sender_label.set_visible(False)
        self.avatar.set_visible(False)
        self.set_halign(Gtk.Align.END)
        self.message_label.set_margin_start(108)
        self.message_label.set_halign(Gtk.Align.END)
        self.message_label.set_justify(Gtk.Justification.RIGHT)
        self.message_label.get_style_context().add_class('message-out')
        self.status_box.set_halign(Gtk.Align.END)

    def set_message_in(self):
        self.sender_label.set_visible(True)
        self.avatar.set_visible(True)
        self.set_halign(Gtk.Align.START)
        self.message_label.set_margin_end(108)
        self.message_label.set_halign(Gtk.Align.START)
        self.message_label.set_justify(Gtk.Justification.LEFT)
        self.message_label.get_style_context().add_class('message-in')
        self.status_box.set_halign(Gtk.Align.START)

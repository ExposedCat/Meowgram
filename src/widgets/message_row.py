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

from gi.repository import Gtk

from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/messagerow.ui")
class MessageRow(Gtk.Box):
    __gtype_name__ = 'MessageRow'

    avatar = Gtk.Template.Child()
    message_label = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)

        try:
            self.message_label.set_text(message.message)
        except AttributeError as error:
            self.message_label.set_text("Message type is not supported yet")
        if message.out:
            self.set_message_out()
        else:
            self.set_message_in()

    def set_message_out(self):
        self.avatar.set_visible(False)
        self.message_label.set_margin_start(108)
        self.message_label.set_halign(Gtk.Align.END)
        self.message_label.set_justify(Gtk.Justification.RIGHT)
        self.message_label.get_style_context().add_class('message-out')
        self.read_status.set_halign(Gtk.Align.END)

    def set_message_in(self):
        self.avatar.set_visible(True)
        self.message_label.set_margin_end(108)
        self.message_label.set_halign(Gtk.Align.START)
        self.message_label.set_justify(Gtk.Justification.LEFT)
        self.message_label.get_style_context().add_class('message-in')
        self.read_status.set_halign(Gtk.Align.START)

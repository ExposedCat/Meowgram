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

from gi.repository import Gtk, Handy

from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/contactrow.ui")
class ContactRow(Handy.ActionRow):
    __gtype_name__ = 'ContactRow'

    avatar = Gtk.Template.Child()
    read_status = Gtk.Template.Child()
    pin_status = Gtk.Template.Child()
    unread_label = Gtk.Template.Child()
    time_label = Gtk.Template.Child()

    def __init__(self, dialog_data, **kwargs):
        super().__init__(**kwargs)

        self.dialog_data = dialog_data

        self.add_prefix(self.avatar)
        self.set_message_status()
        self.set_unread_status()

        self.set_title(self.get_contact_name())
        self.set_subtitle(self.get_last_message())
        self.time_label.set_label(self.get_last_message_time())

    def get_contact_name(self):
        try:
            contact_name = getattr(self.dialog_data, 'title', self.dialog_data.name)
            if self.dialog_data.entity.verified:
                contact_name = f"{contact_name} ✓"
            return contact_name
        except Exception as error:
            print(f"Error {error}")
            return ""

    def get_last_message(self):
        try:
            last_message = self.dialog_data.message.message.split('\n')[0].strip()
            if self.dialog_data.message.media:
                last_message = "🖼️ Photo"

            if self.dialog_data.message.out:
                sender = "You: "
            elif self.dialog_data.is_user and not self.dialog_data.message.out:
                sender = ""
            else:
                sender = f"{self.dialog_data.message.sender.first_name}: "
            return "".join([sender, last_message])
        except Exception as error:
            print(f"Error {error}")
            return ""

    def get_last_message_time(self):
        try:
            last_message_time = self.dialog_data.message.date \
                .replace(tzinfo=datetime.timezone.utc) \
                .astimezone()

            today = datetime.datetime.now().astimezone()
            days_difference = (today - last_message_time).days

            if days_difference < 1:
                # TODO Make this work with military time
                format_string = '%I∶%M %p'  # 08:57 AM
            elif 1 <= days_difference < 7:
                format_string = '%a'  # Fri
            elif days_difference >= 7:
                format_string = '%b %d'  # Apr 08
            return last_message_time.strftime(format_string)
        except Exception as error:
            print(f"Error {error}")
            return ""

    def set_unread_status(self):
        try:
            is_pinned = self.dialog_data.pinned
            unread_count = self.dialog_data.unread_count
            self.unread_label.set_visible(unread_count)
            self.unread_label.set_label(str(unread_count))
            self.pin_status.set_visible(is_pinned)

            if unread_count and is_pinned:
                self.pin_status.set_visible(False)
        except Exception as error:
            print(f"Error {error}")

    def set_message_status(self):
        try:
            self.read_status.set_visible(self.dialog_data.message.out)
        except Exception as error:
            print(f"Error {error}")

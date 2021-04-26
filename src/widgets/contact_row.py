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

    time_label = Gtk.Template.Child()
    avatar = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    def __init__(self, dialog_data, **kwargs):
        super().__init__(**kwargs)

        self.dialog_data = dialog_data
        self.add_prefix(self.avatar)
        self.set_last_message_is_sent()

        self.set_title(self.get_contact_name())
        self.set_subtitle(self.get_last_message())
        self.time_label.set_label(self.get_last_message_time())

    def get_contact_name(self):
        try:
            contact_name = self.dialog_data.title if hasattr(self.dialog_data, 'title') else self.dialog_data.name
            if self.dialog_data.entity.verified:
                contact_name = f"{contact_name} ✓"
        except Exception as error:
            print(f"Error {error}")
            contact_name = ""
        finally:
            return contact_name

    def get_last_message(self):
        try:
            last_message = self.dialog_data.message.message.split('\n')[0].strip()
            if self.dialog_data.message.media:
                last_message = "🖼️ Photo"
        except Exception as error:
            print(f"Error {error}")
            last_message = ""
        finally:
            if self.dialog_data.message.out:
                return f"You: {last_message}"
            else:
                return last_message

    def get_last_message_time(self):
        try:
            last_message_time = self.dialog_data.message.date
            today = datetime.datetime.now().astimezone()
            days_difference = (today - last_message_time).days
            last_message_time = last_message_time.replace(tzinfo=datetime.timezone.utc).astimezone()

            if days_difference <= 1:
                last_message_time = last_message_time.strftime('%I:%M %p')  # 08:57 AM
            elif days_difference < 7:
                last_message_time = last_message_time.strftime('%a')  # Fri
            elif days_difference >= 7:
                last_message_time = last_message_time.strftime('%b %d')  # Apr 08
        except Exception as error:
            print(f"Error {error}")
            last_message_time = ""
        finally:
            return last_message_time

    def set_last_message_is_sent(self):
        try:
            print(self.dialog_data.message.out)
            self.read_status.set_visible(self.dialog_data.message.out)
        except Exception as error:
            print(f"Error {error}")

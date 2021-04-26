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

from gi.repository import Gtk, Handy

from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/contactrow.ui")
class ContactRow(Handy.ActionRow):
    __gtype_name__ = 'ContactRow'

    time_label = Gtk.Template.Child()
    avatar = Gtk.Template.Child()

    def __init__(self, dialog_data, **kwargs):
        super().__init__(**kwargs)

        self.add_prefix(self.avatar)

        contact_name = dialog_data.title if hasattr(dialog_data, 'title') else dialog_data.name
        if dialog_data.entity.verified:
            contact_name = f"{contact_name} ✓"

        last_message = dialog_data.message.message
        last_message_time = dialog_data.message.date.strftime('%H∶%M∶%S')

        self.set_title(contact_name)
        self.set_subtitle(last_message.split("\n")[0].strip())
        self.time_label.set_label(last_message_time)

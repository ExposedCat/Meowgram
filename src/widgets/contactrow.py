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


@Gtk.Template(resource_path="/com/github/ExposedCat/Meowgram/ui/contactrow.ui")
class ContactRow(Handy.ActionRow):
    __gtype_name__ = "ContactRow"

    time_label = Gtk.Template.Child()
    avatar = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_prefix(self.avatar)
        self.set_title("Lorem Ipsum")
        self.set_subtitle("Hello there. How are you?")
        self.time_label.set_label("22∶05")

# context_menu.py
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


class ContextMenu(Gtk.PopoverMenu):

    def __init__(self, menu_type):
        super().__init__()

        builder = Gtk.Builder()
        builder.add_from_resource(f'{Constants.PATHID}/ui/context_menus.ui')
        menu_model = builder.get_object(f'{menu_type}_menu')
        self.set_menu_model(menu_model)

    def show(self, widget):
        self.set_parent(widget)
        self.set_position(Gtk.PositionType.BOTTOM)
        self.popup()

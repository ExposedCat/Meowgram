# window.py
#
# Copyright 2021 mew
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
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', '1')
from gi.repository import Gdk, Gio, GLib, Gtk, Handy


@Gtk.Template(resource_path='/com/github/ExposedCat/Meowgram/window.ui')
class MeowgramWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'MeowgramWindow'

    menu_button = Gtk.Template.Child()
    submenu_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.popover_init()

    def popover_init(self):

        builder = Gtk.Builder()
        builder.add_from_resource('/com/github/ExposedCat/Meowgram/menus.ui')
        menu_model = builder.get_object('primary_menu')
        popover = Gtk.Popover.new_from_model(self.menu_button, menu_model)
        self.menu_button.set_popover(popover)

        submenu_model = builder.get_object('submenu')
        popover = Gtk.Popover.new_from_model(self.submenu_button, submenu_model)
        self.submenu_button.set_popover(popover)
        

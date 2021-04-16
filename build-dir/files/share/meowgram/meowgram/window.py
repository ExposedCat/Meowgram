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
    __gtype_name__ = 'meowgram_window'

    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

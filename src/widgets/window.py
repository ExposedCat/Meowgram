# window.py
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

from gi.repository import Gtk, Handy, GObject

from meowgram.widgets.contactrow import ContactRow
from meowgram.widgets.messagerow import MessageRow


@Gtk.Template(resource_path='/com/github/ExposedCat/Meowgram/ui/window.ui')
class MeowgramWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'MeowgramWindow'

    headerbar_group = Gtk.Template.Child()
    main_leaflet = Gtk.Template.Child()
    contacts_listbox = Gtk.Template.Child()
    message_box = Gtk.Template.Child()

    back_button = Gtk.Template.Child()
    menu_button = Gtk.Template.Child()
    submenu_button = Gtk.Template.Child()

    search_button = Gtk.Template.Child()
    search_revealer = Gtk.Template.Child()

    send_message_revealer = Gtk.Template.Child()
    message_tool_revealer = Gtk.Template.Child()
    message_entry = Gtk.Template.Child()

    channel_flap = Gtk.Template.Child()
    sidebar_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_leaflet.bind_property('folded', self.back_button, 'visible')
        self.main_leaflet.bind_property('folded', self.headerbar_group, 'decorate-all')
        self.search_button.bind_property('active', self.search_revealer, 'reveal-child')
        self.sidebar_button.bind_property('active', self.channel_flap, 'reveal-flap',
                                          GObject.BindingFlags.BIDIRECTIONAL)
        self.popover_init()

        for index in range(10):
            self.contacts_listbox.insert(ContactRow(), -1)
            self.message_box.add(MessageRow(index % 2))

    @Gtk.Template.Callback()
    def on_contacts_activated(self, listbox, row):
        self.main_leaflet.set_visible_child_name('messages_pane')

    @Gtk.Template.Callback()
    def on_back_button_clicked(self, button):
        self.main_leaflet.set_visible_child_name('contacts_pane')

    @Gtk.Template.Callback()
    def on_message_entry_changed(self, entry):
        is_there_text = entry.get_text()
        self.message_tool_revealer.set_reveal_child(not is_there_text)
        self.send_message_revealer.set_reveal_child(is_there_text)

    def popover_init(self):
        builder = Gtk.Builder()
        builder.add_from_resource('/com/github/ExposedCat/Meowgram/ui/menus.ui')
        menu_model = builder.get_object('primary_menu')
        popover = Gtk.Popover.new_from_model(self.menu_button, menu_model)
        self.menu_button.set_popover(popover)

        submenu_model = builder.get_object('submenu')
        popover = Gtk.Popover.new_from_model(self.submenu_button, submenu_model)
        self.submenu_button.set_popover(popover)

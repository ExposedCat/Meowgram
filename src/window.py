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

from gi.repository import Gtk, Handy


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_leaflet.bind_property("folded", self.back_button, "visible")
        self.main_leaflet.bind_property("folded", self.headerbar_group, "decorate-all")
        self.search_button.bind_property("active", self.search_revealer, "reveal-child")
        self.popover_init()

        for index in range(10):
            self.contacts_listbox.insert(ContactRow(), -1)
            self.message_box.add(MessageRow(index % 2))

    @Gtk.Template.Callback()
    def on_back_button_clicked(self, widget):
        self.main_leaflet.set_visible_child_name("contacts_pane")

    def popover_init(self):
        builder = Gtk.Builder()
        builder.add_from_resource('/com/github/ExposedCat/Meowgram/ui/menus.ui')
        menu_model = builder.get_object('primary_menu')
        popover = Gtk.Popover.new_from_model(self.menu_button, menu_model)
        self.menu_button.set_popover(popover)

        submenu_model = builder.get_object('submenu')
        popover = Gtk.Popover.new_from_model(self.submenu_button, submenu_model)
        self.submenu_button.set_popover(popover)


@Gtk.Template(resource_path='/com/github/ExposedCat/Meowgram/ui/contact.ui')
class ContactRow(Handy.ActionRow):
    __gtype_name__ = 'ContactRow'

    time_label = Gtk.Template.Child()
    avatar = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_prefix(self.avatar)
        self.set_title("USERNAME")
        self.set_subtitle("Hello There")
        self.time_label.set_label("22∶05")


@Gtk.Template(resource_path='/com/github/ExposedCat/Meowgram/ui/message.ui')
class MessageRow(Gtk.Box):
    __gtype_name__ = 'MessageRow'

    avatar = Gtk.Template.Child()
    message_label = Gtk.Template.Child()
    read_status = Gtk.Template.Child()

    def __init__(self, is_from_self, **kwargs):
        super().__init__(**kwargs)

        self.message_style_context = self.message_label.get_style_context()

        if is_from_self:
            self.set_message_in()
        else:
            self.set_message_out()

    def set_message_in(self):
        self.avatar.set_visible(False)
        self.message_label.set_margin_start(72)
        self.message_label.set_halign(Gtk.Align.END)
        self.message_label.set_justify(Gtk.Justification.RIGHT)
        self.message_style_context.add_class("message-out")
        self.read_status.set_halign(Gtk.Align.END)

    def set_message_out(self):
        self.avatar.set_visible(True)
        self.message_label.set_margin_end(72)
        self.message_label.set_halign(Gtk.Align.START)
        self.message_label.set_justify(Gtk.Justification.LEFT)
        self.message_style_context.add_class("message-in")
        self.read_status.set_halign(Gtk.Align.START)

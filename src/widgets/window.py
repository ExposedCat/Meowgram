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

import logging

from gi.repository import Gtk, Handy, GObject, GLib

from meowgram.constants import Constants
from meowgram.connectors.dialogs import dialogs_manager
from meowgram.connectors.messages import messages_manager


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/window.ui")
class MeowgramWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'MeowgramWindow'

    headerbar_group = Gtk.Template.Child()
    messages_headerbar = Gtk.Template.Child()

    main_leaflet = Gtk.Template.Child()
    contacts_listbox = Gtk.Template.Child()
    messages_listbox = Gtk.Template.Child()

    back_button = Gtk.Template.Child()
    search_button = Gtk.Template.Child()
    search_revealer = Gtk.Template.Child()
    sidebar_button = Gtk.Template.Child()
    channel_flap = Gtk.Template.Child()

    send_message_revealer = Gtk.Template.Child()
    message_tool_revealer = Gtk.Template.Child()
    message_entry = Gtk.Template.Child()

    messages_adjustment = Gtk.Template.Child()

    messages_view = Gtk.Template.Child()
    empty_view = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_leaflet.bind_property('folded', self.back_button, 'visible')
        self.main_leaflet.bind_property('folded', self.headerbar_group, 'decorate-all')
        self.search_button.bind_property('active', self.search_revealer, 'reveal-child')
        self.sidebar_button.bind_property('active', self.channel_flap, 'reveal-flap',
                                          GObject.BindingFlags.BIDIRECTIONAL)

        dialogs_manager.show_dialogs(self)
        self.update_view()

        # TODO add button to scroll down

    def scroll_to_bottom_messages(self):
        GLib.timeout_add(
            50, lambda: self.messages_adjustment.set_value(
                self.messages_adjustment.get_upper()
            )
        )

    def update_view(self):
        if self.contacts_listbox.get_selected_row():
            self.channel_flap.set_content(self.messages_view)
            self.sidebar_button.set_visible(True)
        else:
            self.channel_flap.set_content(self.empty_view)
            self.sidebar_button.set_visible(False)

        # TODO animate this

    def update_headerbar(self, contact):
        try:
            contact_name = contact.get_contact_name()
            if not (subtitle := contact.get_room_members_count()):
                # TODO include here also the number of onlined members
                subtitle = contact.get_last_active()
            if contact.get_is_bot():
                subtitle = "bot"
        except AttributeError:
            contact_name = subtitle = ""

        try:
            if contact.chat_id.user_id == 777000:
                subtitle = "service notifications"
        except AttributeError:
            pass

        self.messages_headerbar.set_title(contact_name)
        self.messages_headerbar.set_subtitle(subtitle)

    @Gtk.Template.Callback()
    def on_messages_adjustment_changed(self, adjustment):
        if not adjustment.get_value():
            print("you have reached the top of messages")

    @Gtk.Template.Callback()
    def on_contacts_activated(self, listbox, row):
        self.main_leaflet.set_visible_child_name('messages_pane')

        try:
            contact = row.get_child()
            self.update_headerbar(contact)
            messages_manager.show_messages(self, contact.chat_id)
            self.scroll_to_bottom_messages()
        except AttributeError:
            pass  # This means that there is no selected row, so don't show messages

        self.update_view()

    @Gtk.Template.Callback()
    def on_back_button_clicked(self, button):
        self.contacts_listbox.unselect_all()
        self.main_leaflet.set_visible_child_name('contacts_pane')
        self.update_headerbar(None)

    @Gtk.Template.Callback()
    def on_message_entry_changed(self, entry):
        is_there_text = entry.get_text()
        self.message_tool_revealer.set_reveal_child(not is_there_text)
        self.send_message_revealer.set_reveal_child(is_there_text)

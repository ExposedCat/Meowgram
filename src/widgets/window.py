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

from gi.repository import Gtk, Adw, GObject, GLib, Gio

from meowgram.widgets.dialog_row import DialogRow
from meowgram.widgets.message_row import MessageRow
from meowgram.connectors.dialogs import dialogs_manager
from meowgram.connectors.messages import messages_manager
from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.PATHID}/ui/window.ui")
class MeowgramWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'MeowgramWindow'

    messages_headerbar = Gtk.Template.Child()

    main_leaflet = Gtk.Template.Child()
    contacts_pane = Gtk.Template.Child()
    messages_pane = Gtk.Template.Child()

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

    scrolldown_button_revealer = Gtk.Template.Child()

    contact_name_mem = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_leaflet.bind_property('folded', self.back_button, 'visible')
        self.search_button.bind_property('active', self.search_revealer, 'reveal-child')
        self.sidebar_button.bind_property('active', self.channel_flap, 'reveal-flap',
                                          GObject.BindingFlags.BIDIRECTIONAL)

        self.load_window_size()
        dialogs_manager.show_dialogs(self)
        self.update_view()

        # TODO Use sourceview instead of GtkEntry

        # TODO Seperate other widgets to separate files

        # TODO fix this workaround to not select any on start

    def scroll_to_bottom_messages(self):
        GLib.timeout_add(
            50, lambda: self.messages_adjustment.set_value(
                self.messages_adjustment.get_upper()
            )
        )
        # TODO animate this

    def update_view(self):
        if self.contacts_listbox.get_selected_row():
            self.channel_flap.set_content(self.messages_view)
            self.sidebar_button.set_visible(True)
        else:
            self.channel_flap.set_content(self.empty_view)
            self.sidebar_button.set_visible(False)

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

        # self.messages_headerbar.set_title(contact_name)
        # self.messages_headerbar.set_subtitle(subtitle)

    def update_contacts_listbox(self, dialogs):
        for dialog in dialogs:
            self.contacts_listbox.insert(DialogRow(dialog), -1)

    def update_messages_listbox(self, messages):
        # current_messages = self.messages_listbox.get_children()
        # for message in current_messages:
        #     self.messages_listbox.remove(message)

        for message in reversed(messages):
            contact_name = message.sender.username
            message_row = MessageRow(message)
            message_row.set_as_group(self.contact_name_mem == contact_name)
            self.contact_name_mem = contact_name
            self.messages_listbox.insert(message_row, -1)

    def save_window_size(self):
        settings = Gio.Settings(Constants.APPID)
        size = (
            self.get_size(Gtk.Orientation.HORIZONTAL),
            self.get_size(Gtk.Orientation.VERTICAL)
        )

        settings.set_value('window-size', GLib.Variant('ai', [*size]))

    def load_window_size(self):
        settings = Gio.Settings(Constants.APPID)
        size = settings.get_value('window-size')

        self.set_default_size(*size)

    @Gtk.Template.Callback()
    def on_scrolldown_button_clicked(self, button):
        self.scroll_to_bottom_messages()

        # TODO only show when scrolling down

    @Gtk.Template.Callback()
    def on_messages_adjustment_changed(self, adjustment):
        if not adjustment.get_value():
            print("you have reached the top of messages")

        is_up = adjustment.get_value() != adjustment.get_upper() - adjustment.get_page_size()
        self.scrolldown_button_revealer.set_reveal_child(is_up)

    @Gtk.Template.Callback()
    def on_contacts_activated(self, listbox, row):
        self.main_leaflet.set_visible_child(self.messages_pane)

        try:
            contact = row.get_child()
            self.update_headerbar(contact)
            messages_manager.show_messages(self, contact.chat_id)
            self.scroll_to_bottom_messages()
        except AttributeError as error:
            logging.debug(error)
            # This means that there is no selected row, so don't show messages

        self.update_view()

    @Gtk.Template.Callback()
    def on_back_button_clicked(self, button):
        if selected_row := self.contacts_listbox.get_selected_row():
            self.contacts_listbox.unselect_row(selected_row)

        self.contacts_listbox.unselect_all()
        self.main_leaflet.set_visible_child(self.contacts_pane)
        self.update_headerbar(None)

    @Gtk.Template.Callback()
    def on_message_entry_changed(self, entry):
        is_there_text = entry.get_text()
        self.message_tool_revealer.set_reveal_child(not is_there_text)
        self.send_message_revealer.set_reveal_child(is_there_text)

    @Gtk.Template.Callback()
    def on_send_message_clicked(self, button):
        chat_id = self.contacts_listbox.get_selected_row().get_child().chat_id
        message = self.message_entry.get_text()
        result = messages_manager.send_message(chat_id, message)
        print(result)

    @Gtk.Template.Callback()
    def on_window_closed(self, window):
        self.save_window_size()

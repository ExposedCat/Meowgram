# login.py
#
# Copyright 2021 Gleb Smirnov <glebsmirnov0708@gmail.com>
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
#
# SPDX-License-Identifier: GPL-3.0-or-later

import re

from gi.repository import Gtk, Handy
from meowgram.connectors.login import login_manager
from meowgram.meowgram_constants import meowgram_constants as constants


PHONE_NUMBER = 0
CONFIRM_CODE = 1
PASSWORD = 2


@Gtk.Template(resource_path=constants['RESOURCEID'] + '/ui/loginwindow.ui')
class MeowgramLoginWindow(Handy.Window):
    __gtype_name__ = 'MeowgramLoginWindow'

    next_button = Gtk.Template.Child()
    prev_button = Gtk.Template.Child()

    page_carousel = Gtk.Template.Child()

    phone_page = Gtk.Template.Child()
    confirm_code_page = Gtk.Template.Child()
    password_page = Gtk.Template.Child()

    phone_number = Gtk.Template.Child()
    confirm_code_tg = Gtk.Template.Child()
    confirm_code_sms = Gtk.Template.Child()
    password = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def clear_entries(self, *_):
        for entry in [
            self.phone_number,
            self.confirm_code_tg,
            self.confirm_code_sms,
            self.password,
        ]:
            entry.set_text('')

    @Gtk.Template.Callback()
    def on_text_changed(self, entry):
        text = entry.get_text()
        can_click_next = text != ''
        if entry.props.input_purpose == Gtk.InputPurpose.PHONE:
            text = re.sub(r'[^+\d \-()]', '', text)
            can_click_next = not bool(re.fullmatch(r'\D*', text))
        elif entry.props.input_purpose == Gtk.InputPurpose.DIGITS:
            text = re.sub(r'\D', '', text)
            can_click_next = bool(
                re.fullmatch('\\d{%s}' % entry.get_max_length(), text)
            )
        if text != entry.get_text():
            entry.error_bell()
            entry.set_text(text)
        self.next_button.set_sensitive(can_click_next)

    @Gtk.Template.Callback()
    def on_prev_clicked(self, w):
        current_page = self.page_carousel.get_position()
        if current_page == PASSWORD:
            self.page_carousel.remove(self.password_page)
        self.page_carousel.scroll_to(self.phone_page)
        self.prev_button.set_visible(False)
        self.phone_number.grab_focus()

    @Gtk.Template.Callback()
    def on_next_clicked(self, w):
        current_page = self.page_carousel.get_position()
        if current_page == PHONE_NUMBER:
            login_manager.login(self, self.phone_number.get_text())
        elif current_page == CONFIRM_CODE:
            login_manager.send_code(
                self,
                self.confirm_code_tg.get_text() or self.confirm_code_sms.get_text(),
            )
        elif current_page == PASSWORD:
            login_manager.auth_2fa(self, self.password.get_text())
            return
        self.next_button.set_sensitive(False)

    @Gtk.Template.Callback()
    def switch_code_getting_method(self, w, uri):
        current_page = self.confirm_code_page.get_visible_child_name()
        if current_page == 'via-tg':
            self.confirm_code_page.set_visible_child_name('via-sms')
            self.confirm_code_sms.grab_focus()
        elif current_page == 'via-sms':
            self.confirm_code_page.set_visible_child_name('via-tg')
            self.confirm_code_tg.grab_focus()

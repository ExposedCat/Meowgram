# main.py
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

import sys
import logging

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gio, Gtk, Adw, Gdk, GLib

from meowgram.widgets.main_window import MainWindow
from meowgram.widgets.preferences_window import PreferencesWindow
from meowgram.widgets.login_window import LoginWindow
from meowgram.connectors.login import login_manager
from meowgram.backend.asyncio_separator import aio
from meowgram.constants import Constants

logging.basicConfig(level=logging.DEBUG)


class Application(Gtk.Application):
    def __init__(self, version):
        super().__init__(application_id=Constants.APPID,
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.version = version

        GLib.set_application_name("Meowgram")
        GLib.set_prgname(Constants.APPID)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_resource(f'{Constants.PATHID}/ui/style.css')
        display = Gdk.Display.get_default()
        Gtk.StyleContext.add_provider_for_display(
            display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

        self.setup_actions()

        Adw.init()

    def do_activate(self):
        win = self.props.active_window
        if not win:
            auth = login_manager.login(None, None)
            if auth == 2:
                win = MainWindow(application=self)
            else:
                win = LoginWindow(application=self)
        win.present()

    def setup_actions(self):
        simple_actions = [
            ('show-preferences', self.show_preferences_window, ('<Ctrl>comma',)),
            ('show-shortcuts', self.show_shortcuts_window, ('<Ctrl>question',)),
            ('show-about', self.show_about_dialog, None),
            ('quit', self.on_quit, ('<Ctrl>q',)),
        ]

        for action, callback, accel in simple_actions:
            simple_action = Gio.SimpleAction.new(action, None)
            simple_action.connect('activate', callback)
            self.add_action(simple_action)
            if accel:
                self.set_accels_for_action(f'app.{action}', accel)

    def show_main_window(self):
        self.props.active_window.close()
        win = MainWindow(application=self)
        win.present()

    def show_preferences_window(self, action, param):
        preferences = PreferencesWindow()
        preferences.set_transient_for(self.props.active_window)
        preferences.show()

    def show_shortcuts_window(self, action, param):
        builder = Gtk.Builder()
        builder.add_from_resource(f'{Constants.PATHID}/ui/shortcuts_window.ui')
        window = builder.get_object('shortcuts')
        window.set_transient_for(self.props.active_window)
        window.present()

    def show_about_dialog(self, action, param):
        about = Gtk.AboutDialog()
        about.set_transient_for(self.props.active_window)
        about.set_modal(True)
        about.set_version(self.version)
        about.set_program_name("Meowgram")
        about.set_logo_icon_name(Constants.APPID)
        about.set_authors(
            [
                "Artem Prokop",
                "Dave Patrick",
                "Gleb Smirnov",
                "Artem Kudyakov",
                "Alexey Mikhailov"
            ]
        )
        about.set_comments(_("GTK Telegram Client"))
        about.set_wrap_license(True)
        about.set_license_type(Gtk.License.GPL_3_0)
        # Translators: Replace "translator-credits" with your names, one name per line
        about.set_translator_credits(_("translator-credits"))
        about.set_website_label(_("GitHub"))
        about.set_website("https://github.com/ExposedCat/Meowgram")
        about.present()

    def on_quit(self, action, param):
        print("exit")
        # TODO for some reason, this crashes :( IDK why
        aio.stop_thread()
        self.quit()


def main(version):
    app = Application(version)
    return app.run(sys.argv)

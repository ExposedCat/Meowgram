from gi.repository import Adw, Gtk

from meowgram.constants import Constants


@Gtk.Template(resource_path=f'{Constants.PATHID}/ui/preferences_window.ui')
class PreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = "PreferencesWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

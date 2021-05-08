from gi.repository import Adw, Gtk

from meowgram.constants import Constants


@Gtk.Template(resource_path=f"{Constants.RESOURCEID}/ui/preferenceswindow.ui")
class MeowgramPreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = "MeowgramPreferencesWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

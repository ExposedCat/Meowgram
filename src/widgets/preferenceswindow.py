from gi.repository import Handy, Gtk


@Gtk.Template(resource_path="/com/github/ExposedCat/Meowgram/ui/preferenceswindow.ui")
class MeowgramPreferencesWindow(Handy.PreferencesWindow):
    __gtype_name__ = "MeowgramPreferencesWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

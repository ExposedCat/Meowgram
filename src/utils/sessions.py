import gi
gi.require_version('Secret', '1')
from gi.repository import GLib, Secret

SESSION_SCHEMA = Secret.Schema.new(
    "org.mock.type.Store",
    Secret.SchemaFlags.NONE,
    {
        "name": Secret.SchemaAttributeType.STRING
    }
)


class SessionManager:
    def get_sessions(self):
        try:
            sessions = Secret.password_lookup_sync(
                SESSION_SCHEMA, {'name': 'session'}, None
            )
        except GLib.Error as e:
            print(e)
            sessions = None

        if not sessions:
            return None

        return sessions.split('][')

    def add_session(self, session):
        sessions = self.get_sessions()
        if not sessions:
            sessions = session
        else:
            sessions += f'][{session}'

        try:
            Secret.password_store_sync(
                SESSION_SCHEMA, {'name': 'session'}, Secret.COLLECTION_DEFAULT,
                'session', sessions,
                None
            )
        except GLib.Error as e:
            print(e)
            return

        print(self.get_sessions())


session_manager = SessionManager()

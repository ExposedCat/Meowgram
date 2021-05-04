from meowgram.config import API_ID, API_HASH
from telethon import TelegramClient, errors
from telethon.sessions import StringSession

from meowgram.utils.sessions import session_manager


class MeowgramClient:
    client = None
    phone_number = None

    async def login(self, phone_number):  # 0 - error; 1 - need auth; 2 - already authorized
        try:
            session = StringSession()
            if not phone_number:
                existing_sessions = session_manager.get_sessions()
                if existing_sessions:
                    phone_number = existing_sessions[0]
                    session = StringSession(phone_number)
                else:
                    return
            self.client = TelegramClient(session, API_ID, API_HASH)
            self.phone_number = phone_number
            await self.client.connect()
            if not await self.client.is_user_authorized():
                await self.client.send_code_request(phone_number)
                return 1
            else:
                return 2
        except Exception as error:
            print(f"Error {error}")
            return 0

    async def auth_code(self, code):  # 0 - wrong code; 1 - need 2FA; 2 - all is ok
        try:
            await self.client.sign_in(self.phone_number, code)
            self.save_session()
            return 2
        except errors.PhoneCodeInvalidError:
            return 0
        except errors.SessionPasswordNeededError:
            return 1

    async def auth_2fa(self, password):  # 0 - wrong password; 1 - all is ok
        try:
            await self.client.sign_in(password=password)
            self.save_session()
            return 1
        except errors.SrpIdInvalidError:
            return 0

    async def get_dialogs(self):
        dialogs = await self.client.get_dialogs(limit=50)
        return dialogs

    async def get_messages(self, chat_id):
        messages = await self.client.get_messages(chat_id, limit=20)
        return messages

    def save_session(self):
        session_manager.add_session(self.client.session.save())


client = MeowgramClient()

from meowgram.config import API_ID, API_HASH
from meowgram.constants import Constants
from telethon import TelegramClient, errors

from os import listdir


class MeowgramClient:
    client = None
    phone_number = None

    async def login(self, phone_number):
        try:
            # TODO replace searching .session with libsecret
            if not phone_number:
                files = listdir('.')
                print(files)
                existing_session = [filename for filename in files if filename.endswith('.session')]
                if existing_session:
                    phone_number = existing_session.split('.')[0]
                else:
                    print('Unathorized')
            self.client = TelegramClient(str(phone_number), API_ID, API_HASH)
            self.phone_number = phone_number
            await self.client.connect()
            if not await self.client.is_user_authorized():
                print('Not authorized')
                await self.client.send_code_request(phone_number)
            else:
                print('Authorized')
        except Exception as error:
            print(f"Error {error}")

    async def auth_code(self, code):  # 0 - wrong code; 1 - need 2FA; 2 - all is ok
        try:
            await self.client.sign_in(self.phone_number, code)
            return 2
        except errors.PhoneCodeInvalidError:
            return 0
        except errors.SessionPasswordNeededError:
            return 1

    async def auth_2fa(self, password):  # 0 - wrong password; 1 - all is ok
        try:
            await self.client.sign_in(password=password)
            return 1
        except errors.SrpIdInvalidError:
            return 0

    async def get_dialogs(self):
        try:
            dialogs = await self.client.get_dialogs(limit=None)
            return dialogs
        except Exception as error:
            print(f"Error {error}")


client = MeowgramClient()

from meowgram.config import API_ID, API_HASH
from telethon import TelegramClient, errors


class MeowgramClient:
    client = None

    async def login(self, phone_number):
        self.client = TelegramClient(str(phone_number), API_ID, API_HASH)
        await self.client.connect()
        if not self.client.is_user_authorized():
            await self.client.sign_in(phone_number)

    async def auth_code(self, code):  # 0 - wrong code; 1 - need 2FA; 2 - all is ok
        try:
            try:
                await self.client.sign_in(code)
                return 2
            except errors.PhoneCodeInvalidError:
                return 0
        except errors.SessionPasswordNeededError:
            return 1

    async def auth_2fa(self, code):
        try:
            await self.client.sign_in(code)
            return True
        except errors.SrpIdInvalidError:
            return False


client = MeowgramClient()
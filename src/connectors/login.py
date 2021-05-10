from gi.repository import Gio

from meowgram.backend.telegram_client import client
from meowgram.backend.asyncio_separator import aio

from meowgram.constants import Constants


class LoginManager:
    def login(self, window, phone_number):
        request = aio.run(client.login, (phone_number, window))
        auth = request.result()
        if auth == 1:
            window.confirm_code_page.set_visible_child_name('via-tg')
            window.page_carousel.scroll_to(window.confirm_code_page)
            window.prev_button.set_visible(True)
            window.confirm_code_tg.grab_focus()
        return auth

    def send_code(self, window, code):  # 0 - wrong code; 1 - need 2FA; 2 - all is ok
        request = aio.run(client.auth_code, (code,))
        result = request.result()
        if result == 1:
            window.page_carousel.append(window.password_page)
            window.page_carousel.scroll_to(window.password_page)
            window.password.grab_focus()
        elif result == 2:
            self.finish(window)
        else:
            print("Wrong code")

    def auth_2fa(self, window, password):
        request = aio.run(client.auth_2fa, (password,))
        result = request.result()
        if result == 1:
            self.finish(window)
        else:
            print("Wrong password")

    def finish(self, window):
        Gio.Settings(Constants.APPID).set_boolean(
            'logged-in',
            True
        )
        window.props.application.show_main_window()


login_manager = LoginManager()

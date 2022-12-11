from data.model import User
from data.services import UserServices


class UserHandlers:
    services: UserServices

    def __init__(self, services: UserServices):
        self.services = services

    def sign_up(self, username: str, password: str) -> None:
        username = username.strip().lower()
        password = password.strip()

        if not self._validate_username_and_password(username, password):
            return None

        self.services.create_user(username=username, password=password)

    def sign_in(self, username: str, password: str) -> User | None:
        username = username.strip().lower()
        password = password.strip()

        if not self._validate_username_and_password(username, password):
            return None

        return self.services.get_user(username=username, password=password)

    @staticmethod
    def _validate_username_and_password(username: str, password: str) -> bool:
        if username.startswith(' '):
            print('username is invalid')
            return False

        if len(password) < 8:
            print('password is too short')
            return False

        return True

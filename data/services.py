from data.model import User
from data.repository import UserRepositories


class UserServices:

    repos: UserRepositories

    def __init__(self, repositories: UserRepositories):
        self.repos = repositories

    def create_user(self, username: str, password: str) -> None:
        self.repos.create_user(username=username, password=password)

    def get_user(self, username: str, password: str) -> User | None:
        return self.repos.get_user(username=username, password=password)

    def add_wallet(self, user: User, currency: str):
        self.repos.add_wallet(user=user, currency=currency)

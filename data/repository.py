from dataclasses import dataclass, field

from data.model import User, Wallet


@dataclass
class UserRepositories:
    users_data: list[User] = field(default_factory=list)

    def create_user(self, username: str, password: str) -> None:
        user = User(username=username)
        user.set_password(password=password)

        self.users_data.append(user)

    def get_user(self, username: str, password: str) -> User | None:
        user = next(
            (u for u in self.users_data if username == u.username and u.check_password(password)),
            None
        )

        if not user:
            print('User not found')
            return

        return user

    def get_users(self):
        return self.users_data

    @staticmethod
    def add_wallet(user: User, currency: str, start_amount: float = 0):
        user.add_wallet(currency=currency, start_amount=start_amount)

    @staticmethod
    def convert_money(from_wallet: Wallet, to_wallet: Wallet, currency_from: str, amount: float):
        from_wallet.subtract_money(currency=currency_from, amount=amount)
        to_wallet.add_money(currency=currency_from, amount=amount)



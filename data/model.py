import hashlib
from dataclasses import dataclass, field
from enum import Enum


# class Account
class Currency(Enum):
    USD = 1.0
    KZT = 470.0
    EUR = 0.95
    RUB = 62.52


@dataclass
class Wallet:
    amount: float
    currency: str

    def _convert_money(self, currency: str, amount: float) -> float:
        return amount / Currency[currency].value * Currency[self.currency].value

    def add_money(self, currency: str, amount: float):
        self.amount += self._convert_money(currency=currency, amount=amount)

    def subtract_money(self, currency: str, amount: float):
        if self.amount < self._convert_money(currency=currency, amount=amount):
            return 'Not enough money'
        self.amount -= self._convert_money(currency=currency, amount=amount)

    def set_currency(self, currency: str):
        self.currency = currency

    def __repr__(self):
        return f'{self.currency} {self.amount}'

    def __del__(self):
        print('wallet object destroyed')

@dataclass
class User:
    username: str
    __wallets: list[Wallet] = field(default_factory=list)
    _name: str | None = None
    _surname: str | None = None
    __password: str | None = None

    def add_wallet(self, currency: str, start_amount: float = 0):
        self.__wallets.append(Wallet(currency=currency, amount=start_amount))

    def set_password(self, password: str):
        self.__password = self._hash_password(password)

    def check_password(self, password: str) -> bool:
        return self.__password == self._hash_password(password)

    def get_wallet(self, wallet_type: str) -> Wallet | None:
        wallet = next(
            (w for w in self.__wallets if wallet_type == w.currency),
            None
        )
        return wallet

    def get_wallets(self) -> list[Wallet] | None:
        return self.__wallets

    @staticmethod
    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return f'login:{self.username}'

    def __del__(self):
        del self.__wallets
        print(f'User deleted {self.username}')

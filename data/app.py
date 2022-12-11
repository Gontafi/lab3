import sys

from data.handlers import UserHandlers
from data.model import User, Wallet
from data.repository import UserRepositories
from data.services import UserServices


def init():
    user_repositories = UserRepositories()
    user_services = UserServices(repositories=user_repositories)
    user_handlers = UserHandlers(services=user_services)
    user_handlers.sign_up(username='daryn', password='qweqwe123')
    user_handlers.sign_up(username='Magomed', password='qweqwe123')
    user_handlers.sign_up(username='Alibek', password='qweqwe123')
    user_handlers.sign_up(username='User', password='qweqwe123')
    user_handlers.sign_up(username='Aika', password='qweqwe123')

    while True:
        print('\nAvailable users default:')
        print('username=\'daryn\', password=\'qweqwe123\'')
        print('username=\'Magomed\', password=\'qweqwe123\'')
        print('username=\'Alibek\', password=\'qweqwe123\'')
        print('username=\'User\', password=\'qweqwe123\'')
        print('username=\'Aika\', password=\'qweqwe123\'\n\n')
        print('1.create user')
        print('2.join to user')
        command = input('Enter command or enter q (quit) to exit: ')

        if command == 'q':
            sys.exit(0)

        if command == '1':
            username = input('Enter username:')
            password = input('Enter password:')
            user_handlers.sign_up(username=username, password=password)

        elif command == '2':
            username = input('Enter username:')
            password = input('Enter password:')
            user = user_handlers.sign_in(username=username, password=password)
            if user:
                menu(user_repositories, user)


        else:
            print('invalid command, try again')


def menu(repos: UserRepositories, current_user: User):
    while True:
        print('1.show all users')
        print('2.show wallets')
        print('3.exit')
        command = input()
        match command:
            case '1':
                users: list[User] = repos.get_users()
                for index, user in enumerate(users):
                    print(index, user, sep='.')
                index = int(input('choose one of them:'))
                if 0 <= index < len(users):
                    print('1.transfer money')
                    print('2.exit')
                    inp = input()
                    if inp == '1':
                        wallets = current_user.get_wallets()
                        to_wallets = users[index].get_wallets()
                        from_idx: int
                        to_idx: int
                        if wallets is not None and to_wallets is not None:
                            print('your wallets:')
                            for idx, wallet in enumerate(wallets):
                                print(idx, wallet, sep='.')
                            from_idx = int(input('write wallet index from your wallet to use'))
                            print('user wallets:')
                            for to_idx, wallet in enumerate(to_wallets):
                                print(to_idx, wallet, sep='.')
                            to_idx = int(input('write wallet index from users wallet to use'))
                        else:
                            print("there is no wallet in account")
                            break
                        amount = input('write how many you want to transfer:')
                        repos.convert_money(from_wallet=wallets[from_idx],
                                            to_wallet=to_wallets[to_idx],
                                            currency_from=wallets[from_idx].currency,
                                            amount=float(amount))
                    elif inp == '2':
                        break
            case '2':
                wallets: list[Wallet] = current_user.get_wallets()
                if wallets is not None:
                    for index, wallet in enumerate(wallets):
                        print(index, wallet, sep='.')
                else:
                    print("No wallets.")
                print(f'enter \'add\' to Add Wallet, or any input to go back.')
                inp = input('write command or choose on of wallet:')

                if inp == 'add':
                    currency = input('write currency:')
                    amount = input('write how many you want to transfer:')
                    repos.add_wallet(user=current_user, currency=currency, start_amount=float(amount))

                elif inp.isdigit():
                    index = int(inp)
                    if wallets is not None:
                        if 0 <= index < len(wallets):
                            print(wallets[index])
                            print('1.Add money')
                            print('2.Subtract money')
                            print('3.Transfer between two wallets')
                            inp = input()
                            if inp == '1':
                                currency = input('write currency:')
                                amount = input('write wallet amount:')
                                wallets[index].add_money(currency=currency, amount=int(amount))
                            elif inp == '2':
                                currency = input('write currency:')
                                amount = input('write wallet amount:')
                                wallets[index].subtract_money(currency=currency, amount=int(amount))
                            elif inp == '3':
                                if wallets is not None:
                                    print('your wallets:')
                                    for idx, wallet in enumerate(wallets):
                                        print(idx, wallet, sep='.')
                                    to_idx = int(input('Enter the index of wallet for transfer:'))
                                    amount = input('write how many you want to transfer:')
                                    repos.convert_money(from_wallet=wallets[index],
                                                        to_wallet=wallets[to_idx],
                                                        currency_from=wallets[index].currency,
                                                        amount=float(amount))

            case '3':
                break

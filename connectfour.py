from libs import game


def main():
    """
    The Main Menu for the Connect Four game
    """
    while True:
        x = 0
        while x < 5:
            print()
            x += 1
        print('=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
        print('|    \033[91mC \033[93mO \033[91mN \033[93mN \033[91mE \033[93mC \033[91mT    \033[93mF \033[91mO \033['
              '93mU \033[91mR\033[0m    |')
        print('|       Created by Patrick       |')
        print('|             v0.2.0             |')
        print('| 1 - Singleplayer [WIP]         |')
        print('| 2 - Multiplayer [WIP]          |')
        print('| 3 - Quit                       |')
        print('|                                |')
        print('=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
        print()
        select = input('Make a selection: ').lower().replace(' ', '').strip()
        if select == 'singleplayer' or select == '1':
            game.singleplayer_easy()
        elif select == 'multiplayer' or select == '2':
            x = 0
            while x < 5:
                print()
                x += 1
            print('=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
            print(
                '|    \033[91mC \033[93mO \033[91mN \033[93mN \033[91mE \033[93mC \033[91mT    \033[93mF \033[91mO '
                '\033['
                '93mU \033[91mR\033[0m    |')
            print('|       Created by Patrick       |')
            print('|             v0.2.0             |')
            print('| 1 - Local                      |')
            print('| 2 - Global [WIP]               |')
            print('| 3 - Back                       |')
            print('|                                |')
            print('=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=')
            print()
            select = input('Make a selection: ').lower().replace(' ', '').strip()
            if select == 'local' or select == '1':
                game.multiplayer_local()
            elif select == 'global' or select == '2':
                game.multiplayer_global()
            elif select == 'back' or select == '3':
                pass
            else:
                print('Invalid selection!')
        elif select == 'quit' or select == '3':
            return True
        else:
            print('Invalid selection!')


while True:
    if main():
        break
print('End of Program - Thanks for playing!')

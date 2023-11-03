import check, net


def singleplayer_easy():
    print('This feature is currently unavailable!')

def singleplayer_medium():
    print('This feature is currently unavailable!')

def singleplayer_hard():
    print('This feature is currently unavailable!')


def multiplayer_global():
    net.multiplayer_client()


def multiplayer_local():
    # Define the initial variables
    red = '\033[91m⬤\033[0m'
    yellow = '\033[93m⬤\033[0m'
    winner = False
    empty = '\033[92m〇\033[0m'
    turn = red
    board = [
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty]
    ]
    while True:
        if winner:
            break
        i = 0
        x = 0
        while x < 5:
            print()
            x += 1
        print(f"   1   2    3   4   5    6    7")
        while i < len(board):
            board_row = board[i]
            print(f"----------------------------------")
            print(
                f"| {board_row[0]} | {board_row[1]} | {board_row[2]} | {board_row[3]} | {board_row[4]} | "
                f"{board_row[5]} | {board_row[6]} | ")
            i += 1
        print(f"----------------------------------")
        print(f"Turn: {turn}")
        row = 5
        is_valid = True
        column = check.get_column_select()
        while board[0][column - 1] != empty:
            print('That column is full!')
            is_valid = False
            break

        while row < len(board) and is_valid:
            if board[row][column - 1] == empty:
                board[row][column - 1] = turn
                if check.check_for_winner(board, column - 1, row, turn):
                    i = 0
                    while i < len(board):
                        board_row = board[i]
                        print(f"----------------------------------")
                        print(
                            f"| {board_row[0]} | {board_row[1]} | {board_row[2]} | {board_row[3]} | {board_row[4]} | "
                            f"{board_row[5]} | {board_row[6]} | ")
                        i += 1
                    print(f"{turn} wins!")
                    winner = True
                    break
                if check.check_for_tie(board):
                    i = 0
                    while i < len(board):
                        board_row = board[i]
                        print(f"----------------------------------")
                        print(
                            f"| {board_row[0]} | {board_row[1]} | {board_row[2]} | {board_row[3]} | {board_row[4]} | "
                            f"{board_row[5]} | {board_row[6]} | ")
                        i += 1
                    print(f" {red}/{yellow} Tie!")
                    winner = True
                    break
                if turn == red:
                    turn = yellow
                else:
                    turn = red

                break
            row -= 1
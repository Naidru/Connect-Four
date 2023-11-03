def get_column_select():
    """
    Asks the user to input a non-negative integer \n
    Returns the integer given
    """
    while True:
        print('Select a Column (1-7): ')
        string = input()
        i = 0
        all_chars_are_digits = True
        if string == '':
            all_chars_are_digits = False
            print("Input cannot be empty")
        while i < len(string):
            if (string[i] == '0' or string[i] == '1' or string[i] == '2'
                    or string[i] == '3' or string[i] == '4' or string[i] == '5'
                    or string[i] == '6' or string[i] == '7' or string[i] == '8'
                    or string[i] == '9'):
                pass
            else:
                print('all characters in your input must be numerical.')
                all_chars_are_digits = False
                break
            i += 1
        if all_chars_are_digits:
            if 0 < int(string) <= 7:
                return int(string)
            print('The value is out of range')


def check_for_winner(board, column, row, colour):
    """
    Checks for a winner in the game \n
    Returns Boolean
    """
    # Make sure the column and row are within the range of the board
    column_range = 6
    row_range = 5
    # Check for vertical win
    i = 0
    while i < 3:
        if i > column_range:
            break
        if board[i][column] == colour and board[i + 1][column] == colour and board[i + 2][column] == colour and \
                board[i + 3][column] == colour:
            return True
        i += 1
    # Check for horizontal win
    i = 0
    while i < 4:
        if i > row_range:
            break
        if (board[row][i] == colour and board[row][i + 1] == colour and board[row][i + 2] == colour and board[row]
        [i + 3] == colour):
            return True
        i += 1
    # Check for diagonal win
    i = 0
    while i < 3:
        j = 0
        while j < 4:
            # Check for positive diagonal
            if board[i][j] == colour and board[i + 1][j + 1] == colour and board[i + 2][j + 2] == colour and \
                    board[i + 3][j + 3] == colour:
                return True
            # Check for negative diagonal
            if board[i][j + 3] == colour and board[i + 1][j + 2] == colour and board[i + 2][j + 1] == colour and \
                    board[i + 3][j] == colour:
                return True
            j += 1
        i += 1


def check_for_tie(board):
    """
    Checks for a tie in the game \n
    Returns Boolean
    """
    i = 0
    while i < len(board):
        if board[0][i] == '\033[92m〇\033[0m':
            return False
        i += 1
    return True

def get_port_select():
    """
    Asks the user to input a non-negative integer \n
    Returns the integer given
    """
    while True:
        print('Press Enter for Default Port: 48490')
        print('Select a Port (1025-65536): ')
        port = input()
        i = 0
        all_chars_are_digits = True
        if port == '':
            return 48490
        while i < len(port):
            if (port[i] == '0' or port[i] == '1' or port[i] == '2'
                    or port[i] == '3' or port[i] == '4' or port[i] == '5'
                    or port[i] == '6' or port[i] == '7' or port[i] == '8'
                    or port[i] == '9'):
                pass
            else:
                print('all characters in your port must be numerical.')
                all_chars_are_digits = False
                break
            i += 1
        if all_chars_are_digits:
            if 1024 < int(port) <= 65536:
                return int(port)
            print('Port out of range!')

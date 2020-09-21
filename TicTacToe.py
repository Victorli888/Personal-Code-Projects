import sys
# Game Board
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# Used to reset Board for next game.
reset_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
               'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
               'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

tap = "tap [any key] to continue!"


def ttt_board(board):  # Display Board
    print(board['top-L'] + "|" + board['top-M'] + "|" + board['top-R'])
    print("-+-+-")
    print(board['mid-L'] + "|" + board['mid-M'] + "|" + board['mid-R'])
    print("-+-+-")
    print(board['low-L'] + "|" + board['low-M'] + "|" + board['low-R'])


def player1(board):
    print("Please select from square from the three by three matrix\n "
          "[A,B,C]\n"
          " [D,E,F]\n"
          " [G,H,I]")
    ans = input("> ")
    if ans == "A" and board['top-L'] == " ":
        board['top-L'] = "X"
    elif ans == "B" and board['top-M'] == " ":
        board['top-M'] = "X"
    elif ans == "C" and board['top-R'] == " ":
        board['top-R'] = "X"
    elif ans == "D" and board['mid-L'] == " ":
        board['mid-L'] = "X"
    elif ans == "E" and board['mid-M'] == " ":
        board['mid-M'] = "X"
    elif ans == "F" and board['mid-R'] == " ":
        board['mid-R'] = "X"
    elif ans == "G" and board['low-L'] == " ":
        board['low-L'] = "X"
    elif ans == "H" and board['low-M'] == " ":
        board['low-M'] = "X"
    elif ans == "I" and board['low-R'] == " ":
        board['low-R'] = "X"
    else:
        print("Not valid")
    return board


def player2(board):
    print("Player select from square from the three by three matrix\n "
          "[A,B,C]\n"
          " [D,E,F]\n"
          " [G,H,I]")
    ans = input("> ")
    if ans == "A" and board['top-L'] == " ":
        board['top-L'] = "O"
    elif ans == "B" and board['top-M'] == " ":
        board['top-M'] = "O"
    elif ans == "C" and board['top-R'] == " ":
        board['top-R'] = "O"
    elif ans == "D" and board['mid-L'] == " ":
        board['mid-L'] = "O"
    elif ans == "E" and board['mid-M'] == " ":
        board['mid-M'] = "O"
    elif ans == "F" and board['mid-R'] == " ":
        board['mid-R'] = "O"
    elif ans == "G" and board['low-L'] == " ":
        board['low-L'] = "O"
    elif ans == "H" and board['low-M'] == " ":
        board['low-M'] = "O"
    elif ans == "I" and board['low-R'] == " ":
        board['low-R'] = "O"
    else:
        print("Not Valid")
    return board


def winning_lines(board):  # check for winning lines
    line1 = board['top-L'] == "X" and board['top-M'] == "X" and board['top-R'] == "X"
    line2 = board['mid-L'] == "X" and board['mid-M'] == "X" and board['mid-R'] == "X"
    line3 = board['low-L'] == "X" and board['low-M'] == "X" and board['low-R'] == "X"
    line4 = board['top-L'] == "X" and board['mid-M'] == "X" and board['low-R'] == "X"
    line5 = board['top-R'] == "X" and board['mid-M'] == "X" and board['low-L'] == "X"
    line6 = board['top-L'] == "X" and board['mid-L'] == "X" and board['low-L'] == "X"
    line7 = board['top-M'] == "X" and board['mid-M'] == "X" and board['low-M'] == "X"
    line8 = board['top-R'] == "X" and board['mid-R'] == "X" and board['low-R'] == "X"

    line09 = board['top-L'] == "O" and board['top-M'] == "O" and board['top-R'] == "O"
    line10 = board['mid-L'] == "O" and board['mid-M'] == "O" and board['mid-R'] == "O"
    line11 = board['low-L'] == "O" and board['low-M'] == "O" and board['low-R'] == "O"
    line12 = board['top-L'] == "O" and board['mid-M'] == "O" and board['low-R'] == "O"
    line13 = board['top-R'] == "O" and board['mid-M'] == "O" and board['low-L'] == "O"
    line14 = board['top-L'] == "O" and board['mid-L'] == "O" and board['low-L'] == "O"
    line15 = board['top-M'] == "O" and board['mid-M'] == "O" and board['low-M'] == "O"
    line16 = board['top-R'] == "O" and board['mid-R'] == "O" and board['low-R'] == "O"
    line_check = [line1, line2, line3, line4, line5, line6, line7, line8, line09, line10, line11, line12, line13,
                  line14, line15, line16]
    empty_check = [board['top-M'], board['low-M'], board['mid-L'], board['mid-R'], board['mid-M']]

    if True in line_check:
        print("We have a winner!")
        return False
    return True


def ttt_game(game_Board):  # Main Game logic
    print("Lets start!")
    print(tap)
    # Display Current board
    while winning_lines(game_Board):
        ttt_board(game_Board)
        player1(game_Board)
        if winning_lines(game_Board) is False:  # Check for wins
            break
        ttt_board(game_Board)  # display Board
        player2(game_Board)  # Player 2 Turn
    ttt_board(game_Board)


def start_menu():
    print("Would you like to play Single player? enter [A] for yes.")
    print("type <exit> to quit.")
    ans = input("> ")
    if ans == "A":
        ttt_game(board)
    elif ans == "exit":
        print("Exiting!")
        sys.exit()
    else:
        print("This is not a valid entry")


ttt_game(board)
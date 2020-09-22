import sys
# Game Board
board = [1,2,3,
         4,5,6,
         7,8,9]
# Used to reset Board for next game.
reset_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
               'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
               'low-L': ' ', 'low-M': ' ', 'low-R': ' '}




def print_board(board):  # Display Board
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def player1(board):
    print("Player 1 please select from square from the three by three matrix\n "
          "[1,2,3]\n"
          " [4,5,6]\n"
          " [7,8,9]")
    take_value = True
    while take_value:
        value = input("> ")
        if board[value] is int:
            board[value] = "X"
            break
        else:
            print("That slot has already been marked!")


def player2(board):
    print("Player 2 please select from square from the three by three matrix\n "
          "[1,2,3]\n"
          " [4,5,6]\n"
          " [7,8,9]")
    take_value = True
    while int in board:
        value = input("> ")
        if board[value] is int:
            board[value] = "O"
            break
        else:
            print("That slot has already been marked!")


def winning_lines(board):  # check for winning lines
    w_lines = [(1,2,3), (4,5,6), (7,8,9), (7,4,1), (8,5,1), (9,6,3),(7,5,3),(9,5,1)]
    for i in w_lines:
        if w_lines(i) == ("X","X","X"):
            print("Player 1 Wins")
            return False
        elif w_lines(i) == ("O", "O", "O"):
            print("Player 2 Wins")
            return False
    print("Game Continues")


def ttt_game(game_Board):  # Main Game logic
    print("Lets start!")
    input("tap to continue!")
    no_winner = True
    # Display Current board
    while no_winner:
        print_board(game_Board)
        player1(game_Board)
        no_winner = winning_lines(game_Board)
        print_board(game_Board)  # display Board
        player2(game_Board)  # Player 2 Turn
        no_winner = winning_lines(game_Board)
    print_board(game_Board)


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
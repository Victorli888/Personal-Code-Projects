import sys
# Game Board
board = [0,1,2,
         3,4,5,
         6,7,8]


# Used to reset Board for next game.
def reset_board(board):
    for i in range(0,8):
        board[i] = i
    return board



def print_board(board):  # Display Board
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def player1(board):
    print("Player 1 you will be [X] please select from square from the three by three matrix\n "
          "[0,1,2]\n"
          " [3,4,5]\n"
          " [6,7,8]")
    take_value = True
    while take_value:
        value = input("> ")
        if board[int(value)] is int(value):
            board[int(value)] = "X"
            break
        else:
            print("That slot has already been marked!")


def player2(board):
    print("Player 2 you will be [O] please select from square from the three by three matrix\n "
          "[0,1,2]\n"
          " [3,4,5]\n"
          " [6,7,8]")
    take_value = True
    while take_value:
        value = input("> ")
        if board[int(value)] is int(value):
            board[int(value)] = "O"
            break
        else:
            print("That slot has already been marked!")


def winning_lines(board):  # check for winning lines

    w_lines = [(board[0],board[1],board[2]), (board[3],board[4],board[5]), (board[6],board[7],board[8]),
               (board[6],board[3],board[0]), (board[7],board[4],board[1]), (board[8],board[6],board[2]),
               (board[6],board[4],board[2]), (board[8],board[4],board[0])]
    for i in range(0, 8):
        if w_lines[i] == ("X", "X", "X"):
            print("Player 1 Wins")
            return False

        elif w_lines[i] == ("O", "O", "O"):
            print("Player 2 Wins")
            return False
    print("Game Continues")
    return True


def ttt_game(game_Board):  # Main Game logic
    print("Lets start!")
    input("tap to continue!")
    no_winner = winning_lines(game_Board)
    # Display Current board
    while no_winner:
        print_board(board)
        player1(board)
        no_winner = winning_lines(game_Board)
        if no_winner is False:
            break
        print_board(board)  # display Board
        player2(board)  # Player 2 Turn
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
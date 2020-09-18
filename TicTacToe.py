theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def ttt_board(board):
    print(board['top-L'] + "|" + board['top-M'] + "|" + board['top-R'])
    print("-+-+-")
    print(board['mid-L'] + "|" + board['mid-M'] + "|" + board['mid-R'])
    print("-+-+-")
    print(board['low-L'] + "|" + board['low-M'] + "|" + board['low-R'])


print("Would you like to play [A] Single player or [B] Two Players? choose A or B to proceed")
print("type <exit> to quit.")
ans = input("> ")
while True:  # Main loop for game
    if ans == "A":
        pass  # pass singleplayer method
    elif ans == "B":
        pass  # pass 2 player method
    elif ans == "exit":
        break
    else:
        print("This is not a valid entry")

# ttt_board(theBoard)

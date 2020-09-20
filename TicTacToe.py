theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

reset_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def ttt_board(board):
    print(board['top-L'] + "|" + board['top-M'] + "|" + board['top-R'])
    print("-+-+-")
    print(board['mid-L'] + "|" + board['mid-M'] + "|" + board['mid-R'])
    print("-+-+-")
    print(board['low-L'] + "|" + board['low-M'] + "|" + board['low-R'])


# print("Would you like to play [A] Single player or [B] Two Players? choose A or B to proceed")
# print("type <exit> to quit.")
# ans = input("> ")
# while True:  # Main loop for game
#     if ans == "A":
#         pass  # pass singleplayer method
#     elif ans == "B":
#         pass  # pass 2 player method
#     elif ans == "exit":
#         break
#     else:
#         print("This is not a valid entry")

# ttt_board(theBoard)

def player1 (theBoard):
    print("Please select from square from the three by three matrix\n "
          "[A,B,C]\n"
          " [D,E,F]\n"
          " [G,H,I]")
    ans = input("> ")
    if ans == "A" and theBoard['top-L'] == " ":
        theBoard['top-L'] = "X"
    elif ans == "B" and theBoard['top-M'] == " ":
        theBoard['top-M'] = "X"
    elif ans == "C" and theBoard['top-R'] == " ":
        theBoard['top-R'] = "X"
    elif ans == "D" and theBoard['mid-L'] == " ":
        theBoard['mid-L'] = "X"
    elif ans == "E" and theBoard['mid-M'] == " ":
        theBoard['mid-M'] = "X"
    elif ans == "F" and theBoard['mid-R'] == " ":
        theBoard['mid-R'] = "X"
    elif ans == "G" and theBoard['bot-L'] == " ":
        theBoard['bot-L'] = "X"
    elif ans == "H" and theBoard['bot-M'] == " ":
        theBoard['bot-M'] = "X"
    elif ans == "I" and theBoard['bot-R'] == " ":
        theBoard['bot-R'] = "X"
    else:
        print("Not valid")
    return theBoard


def player2(theBoard):
    print("Player select from square from the three by three matrix\n "
          "[A,B,C]\n"
          " [D,E,F]\n"
          " [G,H,I]")
    ans = input("> ")
    if ans == "A" and theBoard['top-L'] == " ":
        theBoard['top-L'] = "O"
    elif ans == "B" and theBoard['top-M'] == " ":
        theBoard['top-M'] = "O"
    elif ans == "C" and theBoard['top-R'] == " ":
        theBoard['top-R'] = "O"
    elif ans == "D" and theBoard['mid-L'] == " ":
        theBoard['mid-L'] = "O"
    elif ans == "E" and theBoard['mid-M'] == " ":
        theBoard['mid-M'] = "O"
    elif ans == "F" and theBoard['mid-R'] == " ":
        theBoard['mid-R'] = "O"
    elif ans == "G" and theBoard['bot-L'] == " ":
        theBoard['bot-L'] = "O"
    elif ans == "H" and theBoard['bot-M'] == " ":
        theBoard['bot-M'] = "O"
    elif ans == "I" and theBoard['bot-R'] == " ":
        theBoard['bot-R'] = "O"
    else:
        print("Not Valid")
    return theBoard

def winning_lines():
    line1 = theBoard['top-L'] == theBoard['top-M'] and theBoard['top-M'] == theBoard['top-R']
    line2 = theBoard['mid-L'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['mid-R']
    line3 = theBoard['low-L'] == theBoard['low-M'] and theBoard['low-M'] == theBoard['low-R']
    line4 = theBoard['top-L'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['bot-R']
    line5 = theBoard['top-R'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['bot-L']
    line6 = theBoard['top-L'] == theBoard['mid-L'] and theBoard['mid-L'] == theBoard['low-L']
    line7 = theBoard['top-M'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-M']
    line8 = theBoard['top-R'] == theBoard['mid-R'] and theBoard['mid-R'] == theBoard['low-R']

    line_check = [line1, line2, line3, line4, line5, line6, line7, line8]

    if True in line_check:
        print("We have a winner!")



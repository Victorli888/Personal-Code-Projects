import random


def intro():
    print("I am the Magic 8-Ball would you like to ask me a question? (Y/N)")
    q1 = input("> ")
    if q1 == "Y" or q1 == "y":
        start()
    elif q1 == "N" or q1 == "n":
        print("Shutting down...")
    else:
        print("Choose Y or N for Yes or No.")
        intro()


def start():

    print("What is your question? otherwise say \"quit\" ")
    q2 = input("> ")
    if q2 == "quit" or q2 == "Quit" or q2 == "q":
        print("Quiting....")
    else:
        eight_ball = {
 "01": "As I see it, yes.",
 "02": "Ask Again Later.",
 "03": "Best not to tell you now.",
 "04": "My sources say no.",
 "05": "Yes",
 "06": "No",
 "07": "It is certain",
 "08": "Maybe",
 "09": "I can not for see it",
 "10": "This is not so."
    }
        dialogue = []
        dialogue += eight_ball.values()
        print(random.choice(dialogue))
        start()


intro()

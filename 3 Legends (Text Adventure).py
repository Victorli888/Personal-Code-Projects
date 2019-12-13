# Write if statements with and ELSE with an error message to catch errors
# Never nest if statements more than 2 deep and do your best to keep it within 1.
# Keep your Boolean tests simple.

# use a while loop only when you want to loop forever
# other wise you should be using a for loop

# the best way to debug is to print often to see where in the code an error goes wrong
# Waterfall Model Test your code as you go

# Create your text adventure!
# it should have Monsters, Traps, Rooms, etc.
def door(monster):
    print(f"You've entered the domain of the {monster} . You see the beast loom over you."
          "What's your next move?")
    print("1. Attack \n2. Talk \n3. Flee")


def enter():
    choice = input("> ")

    if choice == "1" or "Ox" in choice or "ox" in choice:
        print("entering The door of The Ox")
        door("Minotaur")
        choice = input("> ")
        if choice == "1":  # choice 1 is "Attack"
            print("Attack feature")
            # attack()
        elif choice == "2":
            dialouge_Minotaur()
        elif choice == "3":   # Choice 3 is "Flee"
         print("Flee Feature")
         # flee()
        else:
            print("file dead")
        # There needs to be some sort of pause here to allow user input.


    elif choice == "2" or "Snake" in choice or "snake" in choice:
        print("entering The door of The Snake")
        door("Medusa")
        choice = input("> ")
        if choice == "1":  # choice 1 is "Attack"
            print("Attack Medusa feature")
            # attack()
        elif choice == "2":
            dialouge_Medusa()
        elif choice == "3":  # Choice 3 is "Flee"
            print("Flee Feature Medusa")
            # flee()
        else:
            print("file dead")
        # There needs to be some sort of pause here to allow user input
    elif choice == "3" or "Eye" in choice or "eye" in choice:
        print("entering The door of the The Eye")
        door("Cyclops")
        choice = input("> ")
        if choice == "1":  # choice 1 is "Attack"
            print("Attack feature")
            # attack()
        elif choice == "2":
            dialouge_Cyclops()
        elif choice == "3":  # Choice 3 is "Flee"
            print("Flee Feature")
            # flee()7
        else:
            print("file dead")
        # There needs to be some sort of pause here to allow user input
    else:
        print("You must choose a number to from following.\n1. The Ox\n2. The Snake\n3. The Eye")
        enter()

def dialouge_Minotaur():
    print("You say: Wait let's talk for a second.")
    print("Minotaur: We can talk talk after I take off your legs\n")
    print("How do you respond?\n1. Wait! The Athenian Theseus is hunting you."
          "\n2. I'll have your head then.\n3. *You brace for impact* ")
    choice = input("> ")
    if choice == "1":
        print("Minotaur: What! He who dares to hunt me will die point me his direction.")
    elif choice == "2":
            print("This part of the game has not been developed yet")
            #  attack() User defined function will be added later
    elif choice == "3":
        print("Like a freight train you explode into a puddle of blood as the Minotaur charges "
              "\ninto you. As you memory flashes before you a bright light dawns on you.")
        restart()
    else:
        print("That is not a valid input. Please try again")
        dialouge_Minotaur()

"""
This dialogue for Medusa it is put on hold until the Minotaur dialogue is 
complete.
"""
def dialouge_Medusa():
    print("You say: Wait let's work this out with words")
    print("Medusa: What would you like to talk about? ;) ")
    print("How do you respond?\n1. How about those gorgeous eyes?."
          "\n2. How to lift your curse.\n*Give her the smolder * ")
    choice = input("> ")
    if choice == "1":
        print("As you gaze into her eyes you feel a numbness in your legs.\n"
              "as the coldness overwhelms you, you've become a stone statue.\n"
              "Game Over")

    elif choice == "2":
            print("This part of the game has not been developed yet")
            #  attack() User defined function will be added later
    elif choice == "3":
        print("Like a freight train you explode into a puddle of blood as the Minotaur charges "
              "\ninto you. As you memory flashes before you a bright light dawns on you.")
        restart()
    else:
        print("That is not a valid input. Please try again")
        dialouge_Medusa()

def dialouge_Cyclops():
    print("You say: My one eyed friend lets talk")
    print("Medusa: Me not good at talking, What are we going to talk about? ")
    print("How do you respond?\n1. There's a tasty lamb at the end of this maze. Let me through and\n"
          "and I'll bring you some."
          "\n2. I am nobody and I must enter this door. \n Because if you don't I'll cut out your only eye. ")
    choice = input("> ")
    if choice == "1":
        print("As you gaze into her eyes you feel a numbness in your legs.\n"
              "as the coldness overwhelms you, you've become a stone statue.\n"
              "Game Over")

    elif choice == "2":
            print("This part of the game has not been developed yet")
            #  attack() User defined function will be added later
    elif choice == "3":
        print("Like a freight train you explode into a puddle of blood as the Minotaur charges "
              "\ninto you. As you memory flashes before you a bright light dawns on you.")
        restart()
    else:
        print("That is not a valid input. Please try again")
        dialouge_Medusa()

def restart():
    print("You find yourself back where you started.\n choose your path once more.\n"
          "1. The Ox\n2. The Snake\n3. The Eye")
    enter()






print("""Welcome, You're greeted too a dim dungeon with 3 doors
\neach with the insignia of an Ox a Snake and an Eye.\n
Which door will you enter?""")
print("1. The Ox\n2. The Snake\n3. The Eye")

enter()
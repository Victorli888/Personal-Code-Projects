"""
The issue with this method is I have a counter and it does add up but I don't have something in place if the refuse
the item. I will need to look back on this and see what can be salvaged from this method
"""


def event_text(quantity,item):
    print(f"Congratulations! you have found {quantity} {item}.")
    print("Would you like to add this to your inventory? Please say [Y] or [N]")
    ans = input("> ")

    if ans == "Y" or ans == "y":
        Inventory(quantity, item)
    elif ans == "N" or ans == "n":
        print(f"You walk away and leave {item}")

def Inventory(quantity,item):
    potions = {}
    potions[item] = quantity
    print(potions)
    return potions


event_text(3, "coffee")
print("You walk further down the hall way and you find another box and find more coffee.")
event_text(5, "coffee")
print("\n\nYou check your bag")
input("Press Enter")

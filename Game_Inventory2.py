from collections import Counter

"""
I need to complete two objectives:
1. Create an accessible inventory system
2. Increase and decrease based on player input

1.0 I have issues with running and saving the usable values for Inventory for multible iterations. It can only complete
one iteration before running into issues.
"""


# Player will need to use items in his inventory to complete this inventory

def bag_system(inventory, ans):
    if ans == "A":
        invb = Counter({'potions': 1, 'pokeball': 0})
        inventory = inventory - invb
        print(f"current inventory: {inventory}")
        return inventory
    elif ans == "B":
        print("failed")
        invb = Counter({'potions': 0, 'pokeball': 1})
        inventory = inventory - invb
        print(f"current inventory: {inventory}")
        return inventory
    else:
        binventory = inventory
        print("not a valid answer please try again........")
        ans = input("> ")
        bag_system(binventory, ans)


inventory = Counter({ 'potions':10 , 'pokeball':6})

print(f"current inventory: {inventory}")
print("You are battling Pidgy, would you like to [A] Heal your Pokemon or [B] Capture the Pidgey?")
ans = input("> ")
inventory = bag_system(inventory, ans)
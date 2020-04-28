from collections import Counter

"""
I need to complete two objectives:
1. Create an accessible inventory system
2. Increase and decrease based on player input

Notes:
Inventory subtraction varaible = inv_s In this method we have a counter hash table
that tracks the key-value pair with value being the quantity of that item. we use 
inv_s to subtract a quantity from the value when the item is used.

Else statement simply closes the operation instead of looping because I need a statement
in place to show that we can go back to the previous menu.

Time Complexity O(N)
Space Complexity O(1)
"""


# Player will need to use items in his inventory to complete this inventory

def bag_system(curr_inventory, p_input):
    if p_input == "A":
        inv_s = Counter({'potions': 1, 'pokeball': 0})
        curr_inventory = curr_inventory - inv_s
        print("Using Potion...")
        print(f"current inventory: {curr_inventory}")
        return curr_inventory
    elif p_input == "B":
        print("Using Pokeball...")
        inv_s = Counter({'potions': 0, 'pokeball': 1})
        curr_inventory = curr_inventory - inv_s
        print(f"current inventory: {curr_inventory}")
        return curr_inventory
    else:
        print("not a valid answer exiting operation")
        return curr_inventory


inventory = Counter({'potions': 10, 'pokeball': 6})

print(f"current inventory: {inventory}")
print("You are battling Pidgy, would you like to [A] Heal your Pokemon or [B] Capture the Pidgey?")
ans = input("> ")
inventory = bag_system(inventory, ans)
print("You are battling Pidgy, would you like to [A] Heal your Pokemon or [B] Capture the Pidgey?")
ans = input("> ")
inventory = bag_system(inventory, ans)


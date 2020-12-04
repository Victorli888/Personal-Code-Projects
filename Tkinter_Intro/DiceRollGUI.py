import tkinter as tk
import random

# Event Handler to replace label string name with random integer
def roll_dice():
    lbl_result["text"] = str(random.randint(1,6))

# Create a window and name it "Dice Roll SIM"
window = tk.Tk()
window.title("Dice Roll SIM")
window.columnconfigure(0, minsize=150)
window.rowconfigure([0,1], minsize=50)

# Create Button for "Roll" & display label for Roll Value
btn_roll = tk.Button(text="Roll!", command=roll_dice, highlightbackground='#3E4149')
lbl_result = tk.Label(text="May fortune ever be in your favor")

# Place buttons in appropiate locations using Geometry managers
btn_roll.grid(row=1, stick="news")
lbl_result.grid(row=0)

# Start the program
window.mainloop()

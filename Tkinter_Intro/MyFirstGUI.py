# Create a simple application that simply asks for an input from the user

import tkinter as tk
window = tk.Tk()

# create assets
entry = tk.Entry(fg="yellow", bg="blue", width=50)
label = tk.Label(height=5, width=50, text="Enter a number Here:")

# Pack assets
label.pack()
entry.pack()

window.mainloop()

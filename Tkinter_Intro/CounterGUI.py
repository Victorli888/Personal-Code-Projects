import tkinter as tk

#Generate a window and name it Wowza
window= tk.Tk()
window.title("Wowza")


# create + or - commands using Event Handlers
def inc():
    value = int(lbl_value["text"])
    lbl_value['text'] = f"{value+1}"


def dec():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value-1}"


# Make the window sizeable
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

# Create a decrease button and implement  - command
btn_dec = tk.Button(master=window, highlightbackground='#3E4149', command=dec, text="-")
btn_dec.grid(row=0, column=0, sticky="news")

# Display current value
lbl_value = tk.Label(master=window,  text="0")
lbl_value.grid(row=0, column=1)

# Create a increase button and implement + command
btn_inc = tk.Button(master=window, highlightbackground='#3E4149', command=inc, text="+")
btn_inc.grid(row=0, column=2, sticky="news")

# start the program
window.mainloop()

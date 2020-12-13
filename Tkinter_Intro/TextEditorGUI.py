"""
Create a text editor with
A button for opening a file for editing
A button to save all changes made
A text box to create and edit  the text file.
"""

# Import tkinter library
import tkinter as tk
# Import askopenfilename from tkinter module
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
# Create a window and name it text editor
window = tk.Tk()
window.title("Text Editor")
# make re-configurable window
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# rowconfigure applies only to row index 0
# columncofigure applies only to column index 1


# Create functions for your buttons
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor -{filepath}")


def save_file():
    """Save the current file as a new file"""
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
    # If not filepath, filepath will be None and will return w/o exiting any code
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


# create your buttons
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, bg="gray")  # Frame for the buttons

btn_save = tk.Button(fr_buttons, text="Save As", command=save_file, highlightbackground='#3E4149')
btn_open = tk.Button(fr_buttons, text="Open", command=open_file, highlightbackground='#3E4149')

# Place your buttons on the frame using Geometry Managers
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# Place your btn_frame & Textbox on the window
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="news")

window.mainloop()

import tkinter as tk

# Create a Window "XLDF diff tool"
window = tk.Tk()
window.title("XLDF Diff Tool")

# Frame for xldf
frame_xldf = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

#Pack frame into the window
frame_xldf.pack(fill=tk.BOTH)

# XLDF Fields for entry
prog_fields = ["Location of the 89% XLDFs",
               "Location of the 90% XLDFs",
               "Location of the 91% XLDFs",
               "Location of the 92% XLDFs"]

for i, field in enumerate(prog_fields):
    # Create labels for the fields
    label = tk.Label(master=frame_xldf, text=field)
    entry = tk.Entry(master=frame_xldf, width=88)
    # Use Geometry Manager to organize entry and label
    label.grid(row=i, column=0, sticky="e")
    entry.grid(row=i, column=1)

# Create Buttons to "submit" or "Clear Data"
frame_buttons = tk.Frame(relief=tk.RAISED)
frame_buttons.pack(fill=tk.X, padx=5, pady=5)

btn_submit = tk.Button(master=frame_buttons, bg="green", text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, pady=10)

btn_clear = tk.Button(master=frame_buttons, bg="red", text="Clear")
btn_clear.pack(side=tk.RIGHT, padx=10, pady=10)

# Start application
window.mainloop()


import tkinter as tk

# Create a Window titled "New User Form"
window = tk.Tk()
window.title("New User Form")

# Create a new frame to contain labels and entry widgets
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack(fill=tk.BOTH)

# List of fields to fill out
labels = ["First Name:",
          "Last Name:",
          "Arrival Time",
          "Departure Time",
          "Seat Number:",
          "Requested Meal:"]

# Loop over list of fields to generate labels
for index, field in enumerate(labels):
    # Create labels for the fields, and an entry widget for user input
    label = tk.Label(master=frm_form, text=field)
    entry = tk.Entry(master=frm_form, width=70)
    # Use Geometry manager to place fields and the entry widget in the same row of the index
    label.grid(row=index, column=0, sticky="e")
    entry.grid(row=index, column=1)

# Create buttons "frm_buttons" to submit or clear data
frm_buttons = tk.Frame(relief=tk.RAISED)
frm_buttons.pack(fill=tk.X, padx=5, pady=5, )

btn_submit = tk.Button(master=frm_buttons, bg="green", text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, pady=10)

btn_clear = tk.Button(master=frm_buttons, bg="red", text="Clear")
btn_clear.pack(side=tk.RIGHT, padx=10, pady=10)

# Start application
window.mainloop()

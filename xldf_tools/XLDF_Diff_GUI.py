import tkinter as tk
import compareTool as cT


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



def submit_data():
    per89 = entry1.get()
    per90 = entry2.get()
    per91 = entry3.get()
    per92 = entry4.get()
    cT.start(per89,per90,per91,per92)
    exit()


def exit():
    window.destroy()

# for i, field in enumerate(prog_fields):
#     # Create labels for the fields
#     label = tk.Label(master=frame_xldf, text=field)
#     entry = tk.Entry(master=frame_xldf, width=88)
#
#     # Use Geometry Manager to organize entry and label
#     label.grid(row=i, column=0, sticky="e")
#     entry.grid(row=i, column=1)

# 89 Percent Entry
label1 = tk.Label(master=frame_xldf, text=prog_fields[0])
entry1 = tk.Entry(master=frame_xldf, width=80)
label1.grid(row=0, column=0, sticky="e")
entry1.grid(row=0, column=1)
# 90 Percent Entry
label2 = tk.Label(master=frame_xldf, text=prog_fields[1])
entry2 = tk.Entry(master=frame_xldf, width=80)
label2.grid(row=1, column=0, sticky="e")
entry2.grid(row=1, column=1)
# 91 Percent Entry
label3 = tk.Label(master=frame_xldf, text=prog_fields[2])
entry3 = tk.Entry(master=frame_xldf, width=80)
label3.grid(row=2, column=0, sticky="e")
entry3.grid(row=2, column=1)
# 92 Percent Entry
label4 = tk.Label(master=frame_xldf, text=prog_fields[3])
entry4 = tk.Entry(master=frame_xldf, width=80)
label4.grid(row=3, column=0, sticky="e")
entry4.grid(row=3, column=1)



# Create Buttons to "submit" or "Clear Data"
frame_buttons = tk.Frame(relief=tk.RAISED)
frame_buttons.pack(fill=tk.X, padx=5, pady=5)

btn_submit = tk.Button(master=frame_buttons, command=submit_data, bg="green", text="Run")
btn_submit.pack(side=tk.RIGHT, padx=10, pady=10)

btnExit = tk.Button(master=frame_buttons, command=exit, bg="red", text="Exit")
btnExit.pack(side=tk.RIGHT, padx=10, pady=10)



# Start application
window.mainloop()



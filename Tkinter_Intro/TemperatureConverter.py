# Create a a simple GUI that converts Fahrenheit to Celsius
import tkinter as tk

# Create a Window for Tkinter to work on
window = tk.Tk()
window.title("Temp Convert Widget")
window.resizable(width=False, height=False)


def F2C():
    "Convert from Fahrenheit to Celsius and insert the result into lbl_resultC"
    fahrenheit = enter_dataF.get()
    celsius = (5/9) * (float(fahrenheit)-32)
    lbl_resultC["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


def C2F():
    "Convert from Celsius to Fahrenheit and insert the results into lbl_resultF"
    celsius = enter_dataC.get()
    fahrenheit = ((9/5) * float(celsius) + 32)
    lbl_resultF["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


# Create a frame for entry and label for Fahrenheit to Celsius
frm_entry = tk.Frame(master=window)
enter_dataF = tk.Entry(master=frm_entry, width=10)
lbl_F = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")


# Create similar frame for Celsius to Fahrenheit
frm_entry2 = tk.Frame(master=window)
enter_dataC = tk.Entry(master=frm_entry2, width=10)
lbl_C = tk.Label(master=frm_entry2, text="\N{DEGREE CELSIUS}")

# Create the conversion Button and results display Label
# btn_1 converts from F2C
btn_convert1 = tk.Button(master=window, highlightbackground='#3E4149', text="\N{RIGHTWARDS BLACK ARROW}", command=F2C)

btn_convert2 = tk.Button(master=window, highlightbackground='#3E4149', text="\N{RIGHTWARDS BLACK ARROW}", command=C2F)

# Create the results for the Conversion
# Results for F2C results in Celsius
lbl_resultC = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Results for C2F results in fahrenheit
lbl_resultF = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

# Use Geometry Managers to place
# F2C
enter_dataF.grid(row=0, column=0, sticky="e")
lbl_F.grid(row=0, column=1, sticky="w")

frm_entry.grid(row=0,column=0, padx=10)
btn_convert1.grid(row=0, column=1, pady=10)
lbl_resultC.grid(row=0, column=2, padx=10)

# C2F
enter_dataC.grid(row=1, column=0, sticky="w")
lbl_C.grid(row=1, column=1, sticky="w")

frm_entry2.grid(row=1, column=0, padx=10)
btn_convert2.grid(row=1, column=1, pady=10)
lbl_resultF.grid(row=1, column=2, padx=10)

# Run Application
window.mainloop()

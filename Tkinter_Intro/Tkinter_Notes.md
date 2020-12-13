Link: https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

### Basics
```python
import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label.pack()

window.mainloop()
```
* Import tkinter libary and rename it to tk
* `tk.Tk()`creates the gui window
* `tk.Label()` creates a label to add to the window
* `label.pack()` "packs" the label onto the window
* `window.mainloop()` window.mainloop() tells Python to run the Tkinter event loop
### Gettings User Inputs with Entry Widgets

* Retrieve text with .get()
  * use it to store a value
* Delete text with .delete()
  * deletion starts at but does not include the last index (like string slicing)
  * To delete everything up to and including to use END(). `entry.delete(0,tk.END)` 
* insert text with .insert()
  * insert([index], [what to insert])

Given the following commands,
```python
import tkinter as tk

window = tk.Tk()
text_box = tk.Text()
text_box.pack()
```
 ```
Hello
World

>>> text_box.get("1.0")
'H'

>>> text_box.get("1.0", "1.5")
'Hello'

>>> text_box.get("2.0", "2.5")
'World'

>>> text_box.get("1.0", "tk.END")
'Hello\nWorld\n'

>>> text_box.delete("1.0", "1.5")

World

>>> text_box.insert("1.0", "Hello")
Hello
World

>>> text_box.insert("3.0", ":)")
Hello
World:)

>>> text_box.insert("3.0", "\n:)")
Hello
World
:)

>>> text_box.insert(tk.END, "Hello World :)")
Hello
World
:)
Hello World :)

```

 Frame Widget are important for organizing the layout of the widget in the application
 ```python
import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
```
```python
import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
```

tk.FLAT: Has no border effect (the default value).
tk.SUNKEN: Creates a sunken effect.
tk.RAISED: Creates a raised effect.
tk.GROOVE: Creates a grooved border effect.
tk.RIDGE: Creates a ridged effect.

### Controlling Layout with Geometry Managers

```python
import tkinter as tk

window = tk.Tk()

# Pre-set size
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
label_1 = tk.Label(master=frame1, text="I am Red")
label_1.pack()
frame1.pack()


# Fill to window
frame2 = tk.Frame(master=window, height=100, bg="blue")
frame2.pack(fill=tk.X)
label2 = tk.Label(master=frame2, text="I am blue")
label2.pack()
window.mainloop()
```
to control which Frame a widget is assigned to

`.place()` - controls the precise (x,y)location that a widget should occupy
```python
import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="(0,0)", bg='purple')
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="(75,75)", bg="yellow")
label2.place(y=75, x=75)

window.mainloop()
```

`.grid()` - splits the window or frames into rows and columns
```python
import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        # Geometry Manager 1
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=2
        )
        # Geometry Manager 2
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn{j}")
        label.pack()

window.mainloop()
```
* `frame.grid(row=i, column=j)`
Each frame is attached to the window with .grid() Geometry Manager <br>
* `label.pack()`
Each Label is attached to its master Frame with.pack()<br>
* `padx & pady`
Adds padding in the horizontal and vertical direction
*  `window.columnconfigure(i, weight=1, minsize=75)`<br>

resize using `.columnconfigure()` & `.rowconfigure()` resizes the window object<br>

`weight` attribute determines how the colmun or row should respond to the window resizing<br>

minsize argument keeps makes sure the label widget always displays its text without chopping characters

```python
import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0,1,2,3], minsize=50)

label1 = tk.Label(text='1', bg='purple', fg='yellow')
label2 = tk.Label(text='2', bg='purple', fg='yellow')
label3 = tk.Label(text='1', bg='purple', fg='yellow')
label4 = tk.Label(text='2', bg='purple', fg='yellow')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky='ew')
label3.grid(row=0, column=2, sticky='ns')
label4.grid(row=0, column=3, sticky='news')

window.mainloop()
```
### Using Events and Event Handlers
`window.mainloop()` starts the **event loop**. During the Event loop the application checks for events to execute.
In Tkinter, we write functions called **Event Handlers** for events that happen in our application 

`.bind()` used to bind an event to an event handler

```python
import tkinter as tk
# Create new window and name it test
window = tk.Tk()
window.title("test!")

# Create an event handler
def handle_keypress(event):
    # print associated charcter that was pressed by the key
    print(event.char)

# Bind the keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Start the application
window.mainloop()
```
Bind takes two arguments: .bind(<event_name>, event handler ) <br>
In the above example handle_keypress is bound to "<Key>"
<br> NOTE: print(event.char) occurs in the terminal
<br> 
Let's make a pointless button clicker
```python
import tkinter as tk
# Create new window and name it test
window = tk.Tk()
window.title("test!")


# Event Handler
def handle_click(event):
    print(f"Click me God dammit")

# Create a Button to click on, Highlightbackground changes the color so the button can be seen
button = tk.Button(height=10, width=10,text="Click me!", highlightbackground='#3E4149')
button.pack()

button.bind("<Button-1>", handle_click)

# Start program
window.mainloop()
```
### Using Command
Every button widget has a command attribute that can be assigned to a function, Whenever the button is pressed the<br>
function is executed

```python
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

```
```python
from tkinter.filedialog import askopenfilename
```
From the tkinter.filedialog module import askopenfilename
```python
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open (filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor -{filepath}")
```
Lets Break down this function handler
<br> Lines 321 use askopenfilename dialog from tkinter.filedialog module to display a 
file open dialog and store the selected file path to th `filepath`
<br> Lines 322-323 Checks to if user closes the dialog box or clicks cancel. If True the path is None and will return
without exectuing any code to read the file
<br> Line 324  Delete current contents on the editor before uploading
<br> 325-326 Open selected file and .read() its contents before storing the text as a string
<br> 327 assigns the string of text to text_edit and .insert() the contents to it
<br> 328 Sets the title of the window so that it contains the path of the open file



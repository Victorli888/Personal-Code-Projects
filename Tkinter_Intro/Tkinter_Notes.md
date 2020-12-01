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


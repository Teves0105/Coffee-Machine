import tkinter as tk

def click_button(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        clear_display()
        display.insert(0, "Error")

# Window initialization
# Your code is here
    # The window name is root
root = tk.Tk()
root.title("Simple Calculator")
# Display block initialization
# Your code is here
    # The display Entry widget's name is display
display = tk.Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)
# Buttons initialization
# Your code is here
    # The button list's name is buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("Clear", 4, 1), ("=", 4, 2), ("+", 4, 3),
]
for (text, row, col) in buttons:
    if text == "Clear":
        tk.Button(root, text=text, width=9, height=2, command=lambda: clear_display()).grid(row=row, column=col)
    elif text == "=":
        tk.Button(root, text=text, width=9, height=2, command=lambda: calculate()).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=9, height=2, command=lambda text=text: click_button(text)).grid(row=row, column=col)

root.mainloop()
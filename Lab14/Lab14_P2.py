import tkinter as tk 
import ttkbootstrap as ttk

# window 
window = ttk.Window(themename = 'darkly')
# Your code is here
window.title("Length Converter")
window.geometry("300x150")
# title 
# Your code is here
label = ttk.Label(
    master=window,
    text="Miles to kilometers",
    font="Calibri 24 bold"
)
label.grid(column=0, row=0)
# input field 
# Your code is here
entry_int = ttk.Entry(master=window)
entry_int.grid(column=0, row=1)
# The entry name should be entry_int
def convert():
    mile_input = entry_int.get()
    km_output = float(mile_input) * 1.61
    output_string.set(km_output)
button = ttk.Button(master=window, text="Convert", command=convert)
button.grid(column=0, row=2)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 24', 
    textvariable = output_string)
output_label.grid(column = 0, row = 3)

# run 
window.mainloop()
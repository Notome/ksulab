import tkinter as tk

def increment():
    global COUNTER
    COUNTER += 1
    label.config(text=str(COUNTER))

def decrement():
    global COUNTER
    COUNTER -= 1
    label.config(text=str(COUNTER))

root = tk.Tk()
COUNTER = 0

button_dec = tk.Button(root, text='-', command=decrement)
button_dec.pack(side="left", padx=10, pady=10) 

label = tk.Label(root, text=str(COUNTER)) 
label.pack(side="left", padx=10, pady=10)  

button_inc = tk.Button(root, text='+', command=increment)
button_inc.pack(side="left", padx=10, pady=10) 

root.mainloop()
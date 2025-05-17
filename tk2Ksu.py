import tkinter as tk
import random 

root = tk.Tk()
NUMBER = 0

def get_number():
    global NUMBER  
    NUMBER = random.randint(1, 6) 
    label.config(text=str(NUMBER))  
    
button = tk.Button(root, text='Бросить', command=get_number)
button.pack(side="top", padx=50, pady=0) 

label = tk.Label(root, text=str(NUMBER), font=("Arial", 24))
label.pack(side="top", padx=50, pady=50)  

root.mainloop()
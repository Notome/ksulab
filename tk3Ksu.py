import tkinter as tk

def convert():
    global NUMBER
    try:
        num = float(entry.get())
        NUMBER = (num - 32) * 5/9
        label_result.config(text=f"{NUMBER:.1f} °C")
    except ValueError:
        label_result.config(text="Ошибка ввода")

NUMBER = 0

root = tk.Tk()
root.title("Конвертер °F в °C")

label_fahrenheit = tk.Label(root, text="°F")
label_fahrenheit.grid(row=0, column=0, sticky="e")

entry = tk.Entry(root, width=10)
entry.grid(row=0, column=1, padx=5, pady=10)

button = tk.Button(root, text="→", command=convert)
button.grid(row=0, column=2, padx=5, pady=10)

label_result = tk.Label(root, text="0.0 °C")
label_result.grid(row=0, column=3, padx=5, pady=10)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
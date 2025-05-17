import tkinter as tk

def submit_form():
    data = {labels[i]: entries[i].get() for i in range(len(labels))}
    print("Введенные данные:")
    for key, value in data.items():
        print(f"{key}: {value}")

def clear_form():
    for entry in entries:
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Введите домашний адрес")
labels = ["Имя:", "Фамилия:", "Адрес 1:", "Адрес 2:", "Город:", "Регион:", "Почтовый индекс:", "Страна:"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

button_frame = tk.Frame(root)
button_frame.grid(row=len(labels), column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Очистить", command=clear_form).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Отправить", command=submit_form).pack(side=tk.LEFT, padx=5)

root.mainloop()
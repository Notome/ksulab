import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import io

def plot_and_save():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        x_min = float(entry_xmin.get())
        x_max = float(entry_xmax.get())
        step = float(entry_step.get())
        
        if x_min <= 0:
            status_label.config(text="Ошибка: x должен быть > 0")
            return
            
        x_values = np.arange(x_min, x_max + step, step)
        y_values = a * np.log(x_values) + b
        
        plt.figure()
        plt.plot(x_values, y_values)
        plt.title("f(x) = a·ln(x) + b")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        
        wb = Workbook()
        ws = wb.active
        ws.append(["x", "f(x)"])
        
        for xi, yi in zip(x_values, y_values):
            ws.append([xi, yi])
        
        img = Image(buf)
        img.width = 500
        img.height = 300
        ws.add_image(img, "D2")
        
        wb.save("graph_data.xlsx")
        plt.show()
        
        status_label.config(text="Файл graph_data.xlsx создан")
        
    except ValueError:
        status_label.config(text="Ошибка ввода данных")

root = tk.Tk()
root.title("График функции")

tk.Label(root, text="a:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
entry_a.insert(0, "1.0")

tk.Label(root, text="b:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)
entry_b.insert(0, "0.0")

tk.Label(root, text="x_min (>0):").grid(row=2, column=0)
entry_xmin = tk.Entry(root)
entry_xmin.grid(row=2, column=1)
entry_xmin.insert(0, "0.1")

tk.Label(root, text="x_max:").grid(row=3, column=0)
entry_xmax = tk.Entry(root)
entry_xmax.grid(row=3, column=1)
entry_xmax.insert(0, "10.0")

tk.Label(root, text="Шаг:").grid(row=4, column=0)
entry_step = tk.Entry(root)
entry_step.grid(row=4, column=1)
entry_step.insert(0, "0.1")

plot_button = tk.Button(root, text="Создать график и Excel", command=plot_and_save)
plot_button.grid(row=5, column=0, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
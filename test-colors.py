import tkinter as tk
from tkmacosx import Button

def create_window():

    window = tk.Tk()
    window.title("Цветная кнопка")

    # Создаем кнопку с заданным цветом фона и текстом
    button = Button(window, text="Цветная кнопка", bg="LightBlue", fg="Blue", width=200, height=200)
    button.pack(pady=20)

    window.mainloop()

create_window()
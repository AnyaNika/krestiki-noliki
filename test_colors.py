import tkinter as tk

def create_window():
    # Создаем главное окно
    window = tk.Tk()
    window.title("Цветная кнопка")

    # Создаем кнопку с заданным цветом фона и текстом
    button = tk.Button(window, text="", bg="LightGreen", fg="black", width=20, height=2)

    # Размещаем кнопку в окне
    button.pack(pady=20)

    # Запускаем главный цикл приложения
    window.mainloop()

create_window()
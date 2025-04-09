import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry('300x250')
current_player = "X"
buttons = []
window.config(background='LightBlue')


def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] !="":
            return [(i, 0), (i, 1), (i, 2)]
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] !="":
            return [(0, i), (1, i), (2, i)]

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
        return [(0, 0), (1, 1), (2, 2)]
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
        return [(0, 2), (1, 1), (2, 0)]
    return None


def highlight_winner(winning_coords):
    for (i,j) in winning_coords:
        buttons[i][j].config(fg='Red')


def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] !='':
        return

    buttons[row][col]['text'] = current_player

    winning_coords = check_winner()
    if winning_coords:
        highlight_winner(winning_coords)
        window.update_idletasks()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        reset_game()
    else:
        current_player = "0" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''
            buttons[i][j].config(fg='Black')


for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

reset_btn = tk.Button(window, text="Сброс", font=("Arial", 15), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

window.mainloop()
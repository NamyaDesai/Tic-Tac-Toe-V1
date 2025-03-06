import tkinter as t
from tkinter import messagebox
import random

def check_winner():
    global game_over
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            game_over = True
            return
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        game_over = True


def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not game_over:
        buttons[index]["text"] = current_player
        check_winner()
        if not game_over:
            toggle_player()

            if one_player_mode and current_player == "O":
                computer_move()


def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")


def computer_move():
    empty_buttons = [i for i, button in enumerate(buttons) if button["text"] == ""]
    if empty_buttons:
        index = random.choice(empty_buttons)
        buttons[index]["text"] = "O"
        check_winner()
        if not game_over:
            toggle_player()


def start_two_player():
    global one_player_mode, current_player, game_over
    one_player_mode = False
    current_player = "X"
    game_over = False
    reset_board()
    label.config(text=f"Player {current_player}'s turn")


def start_one_player():
    global one_player_mode, current_player, game_over
    one_player_mode = True
    current_player = "X"
    game_over = False
    reset_board()
    label.config(text=f"Player {current_player}'s turn")


def reset_board():
    for button in buttons:
        button["text"] = ""
        button.config(bg="SystemButtonFace")


# Main window
win = t.Tk()
win.title("Tic Tac Toe")

# Game variables
buttons = [t.Button(win, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]
current_player = "X"
game_over = False
one_player_mode = False

# Layout
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

label = t.Label(win, text="", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Buttons to select game mode
two_player_button = t.Button(win, text="2 Player", font=("normal", 14), command=start_two_player)
two_player_button.grid(row=4, column=0)

one_player_button = t.Button(win, text="1 Player", font=("normal", 14), command=start_one_player)
one_player_button.grid(row=4, column=2)

win.mainloop()

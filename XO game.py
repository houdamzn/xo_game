from tkinter import *
from random import choice

def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        game_btns[row][col]['text'] = player

        if check_winner() == False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

            if player == "O":
                computer_move()

        elif check_winner() == True:
            label.config(text=(player + " wins!"))
        elif check_winner() == 'tie':
            label.config(text=("Tie, No Winner!"))

def A_algorithm():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if game_btns[r][c]['text'] == ""]
    
    if empty_cells:
        return choice(empty_cells)
    else:
        return None

def computer_move():
    move = A_algorithm()
    
    if move:
        row, col = move
        game_btns[row][col].invoke()

def check_winner():
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            highlight_winner_cells([(row, 0), (row, 1), (row, 2)])
            return True

    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            highlight_winner_cells([(0, col), (1, col), (2, col)])
            return True

    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        highlight_winner_cells([(0, 0), (1, 1), (2, 2)])
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        highlight_winner_cells([(0, 2), (1, 1), (2, 0)])
        return True

    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
        return 'tie'
    else:
        return False

def check_empty_spaces():
    return any(game_btns[row][col]['text'] == "" for row in range(3) for col in range(3))

def highlight_winner_cells(cells):
    for cell in cells:
        game_btns[cell[0]][cell[1]].config(bg="cyan")

def start_new_game():
    global player
    player = "O"
    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")

    if player == "X":
        computer_move()
    elif player == "O":
        computer_move()

window = Tk()
window.title("Tic_Tac_Toe")

players = ["X", "O"]
player = choice(players)
game_btns = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=(player, "turn"), font=('consolas', 40))
label.pack(side="top")

restart_btn = Button(text="play", font=('consolas', 20), command=start_new_game)
restart_btn.pack(side='top')

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()

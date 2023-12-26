from tkinter import * 
from glob import glob
from random import choice
import random

#give turn for the auther gamer
def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        # Put player's symbol
        game_btns[row][col]['text'] = player

        if check_winner() == False:
            # Switch player
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

            if player == "O":
                # Computer's move
                computer_move()

        elif check_winner() == True:
         label.config(text=(player + " wins!"))
        elif check_winner() == 'tie':
         label.config(text=("Tie, No Winner!"))




# Computer's move (AI)
def computer_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if game_btns[r][c]['text'] == ""]
    if empty_cells:
        row, col = choice(empty_cells)
        game_btns[row][col].invoke()


#if there is winner (true)
def check_winner(): 
     # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="cyan")
            game_btns[row][1].config(bg="cyan")
            game_btns[row][2].config(bg="cyan")
            return True

    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="cyan")
            game_btns[1][col].config(bg="cyan")
            game_btns[2][col].config(bg="cyan")
            return True

    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][2].config(bg="cyan")
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="cyan")
        game_btns[1][1].config(bg="cyan")
        game_btns[2][0].config(bg="cyan")
        return True

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')

        return 'tie'

    else:
        return False




#if all of them empty game end 
def check_empty_spaces():
     spaces = 9

     for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

     if spaces == 0:
        return False
     else:
        return True


#for starting new game
def start_new_game():
    global player
    player = "O"  # User always starts with 'O'
    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")

    # If the computer is the first player, make its move
    if player == "X":
        computer_move()

    elif player =="O":
        computer_move()
        
window = Tk()
window.title("Tic_Tac_Toe")

players = ["X", "O"]  # our players
player = choice(players)
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

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
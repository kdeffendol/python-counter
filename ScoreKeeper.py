import tkinter as tk
from tkinter import ttk

window = tk.Tk()
score1 = tk.StringVar()
score1.set("0")
score2 = tk.StringVar()
score2.set("0")

def addOne(score):
    score.set(str(int(score.get()) + 1))
    #print(score.get())

def subtractOne(score):
    if (int(score.get()) > 0):
        score.set(str(int(score.get()) - 1))
    #print(score.get())

#player 1
player1Label = ttk.Label(window, text="Player 1 Score: ")
player1Score = ttk.Label(window, textvariable = score1)
player1Label.grid(row=1, column=1)
player1Score.grid(row=1, column=2)

player1Up = ttk.Button(window, text="+", command=lambda: addOne(score1))
player1Up.grid(row=1, column=3)

player1Down = ttk.Button(window, text="-", command=lambda: subtractOne(score1))
player1Down.grid(row=1, column=4)

#player 2 
player2Label = ttk.Label(window, text="Player 2 Score: ")
player2Label.grid(row=2, column=1)
player2Score = ttk.Label(window, textvariable = score2)
player2Score.grid(row=2, column=2)

player2Up = ttk.Button(window, text="+", command=lambda: addOne(score2))
player2Up.grid(row=2, column=3)

player2Down = ttk.Button(window, text="-", command=lambda: subtractOne(score2))
player2Down.grid(row=2, column=4)

#quit program
quit_button = ttk.Button(window, text="Quit")
quit_button.grid(row=3, column=2)
quit_button['command'] = window.destroy

window.mainloop()
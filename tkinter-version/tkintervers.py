import random
import tkinter as tk
from tkinter import messagebox

Body_Parts = ["lips", "genitals", "thigh", "neck", "chest", "foot"]
Acts = ["suck", "lick", "nibble", "caress", "kiss", "massage"]
Players = ["player1", "player2", "player3"]

def roll_dice():
    rp2 = random.sample(Players, 2)
    roll_body = random.choice(Body_Parts)
    roll_act = random.choice(Acts)
    message = f"{rp2}\n{roll_act}\n{roll_body}"
    messagebox.showinfo("Dice Roll Result", message)

root = tk.Tk()
root.title("Sex Dice Game")

frame = tk.Frame(root)
frame.pack(pady=20)

button = tk.Button(frame, text="Roll Dice", command=roll_dice)
button.pack()

root.mainloop()

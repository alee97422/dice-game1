import tkinter as tk
import random
import tkinter.colorchooser as colorchooser

class StartupPage:
    def __init__(self, master):
        self.master = master
        master.title("Sex Dice Game - Startup")

        # Define the widgets
        self.num_players_label = tk.Label(master, text="Number of players:")
        self.num_players_label.pack(pady=(50, 10))
        self.num_players_entry = tk.Entry(master)
        self.num_players_entry.pack(pady=(0, 10))
        self.player_names_label = tk.Label(master, text="Player names (separated by commas):")
        self.player_names_label.pack(pady=(0, 10))
        self.player_names_entry = tk.Entry(master)
        self.player_names_entry.pack(pady=(0, 50))
        color_button = tk.Button(master, text="Choose theme color", command=self.choose_color)
        color_button.pack()
        start_button = tk.Button(master, text="Start Game", command=self.start_game)
        start_button.pack()

        # Store the default color
        self.color = 'white'

    def choose_color(self):
        # Open the color chooser and update the color
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color
            self.master.config(background=color)

    def start_game(self):
        # Parse input and start game
        num_players = int(self.num_players_entry.get())
        player_names = [name.strip() for name in self.player_names_entry.get().split(',')]
        self.master.destroy()
        root = tk.Tk()
        app = SexDiceGameApp(root, num_players, player_names, self.color)
        root.mainloop()




class SexDiceGameApp:
    def __init__(self, master, num_players, player_names, color):
        self.master = master
        master.title("Sex Dice Game")

        # Define the widgets
        self.result_label = tk.Label(master, text='Press the roll button to start the game!', font=('Arial', 30), justify='center', bg=color)
        self.result_label.pack(pady=(50, 10))
        roll_button = RollButton(master, text='Roll the dice!', on_roll=self.on_roll)
        roll_button.pack(pady=(10, 50))
        back_button = tk.Button(master, text="Back", command=self.go_back)
        back_button.pack()

        # Store game data
        self.num_players = num_players
        self.player_names = player_names

    def on_roll(self):
        # Roll the dice and display the result
        body_part = random.choice(Body_Parts)
        act = random.choice(Acts)
        players = random.sample(self.player_names, 2)
        result = f'{players[0]} {act} {players[1]}' + ' ' + 'on the' + ' ' + body_part
        self.result_label.config(text=result)

    def go_back(self):
        # Destroy the game screen and return to the startup screen
        self.master.destroy()
        root = tk.Tk()
        app = StartupPage(root)
        root.mainloop()

class RollButton(tk.Button):
    def __init__(self, master, text='', on_roll=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(text=text, font=('Arial', 20), command=on_roll)

# Define the game data
Body_Parts = ["lips", "genitals","thigh","neck", "chest","foot"]
Acts = ["suck", "lick", "nibble","caress","kiss","massage"]

# Create the startup page
root = tk.Tk()
app = StartupPage(root)
root.mainloop()

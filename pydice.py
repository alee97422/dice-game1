import random

Body_Parts = ["lips", "genitals", "thigh", "neck", "chest", "foot"]
Acts = ["suck", "lick", "nibble", "caress", "kiss", "massage"]

# Ask for the number of players
num_players = int(input("Enter the number of players: "))
Players = [input(f"Enter name for player {i + 1}: ") for i in range(num_players)]

def Roll1():
    rp2 = random.sample(Players, 2)
    Roll_body, Roll_act = random.choice(Body_Parts), random.choice(Acts)
    print(f"{rp2}\n{Roll_act}\n{Roll_body}")

# Create a loop that keeps asking for user input until they decide to stop
while True:
    user_input = input("Press Enter to roll (or type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        break  # Exit the loop if the user types 'exit'
    
    Roll1()

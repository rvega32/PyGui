import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors")

def play_rps(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"
    
    messagebox.showinfo("Result", f"You chose {player_choice}, Computer chose {computer_choice}.\n{result}")
    
    if result == "You win!":
        transition_to_number_game()

    def transition_to_number_game():
        for widget in root.winfo_children():
            widget.destroy()

            tk.Label(root, text="Guess a number between 1 and 100").pack()
            entry = tk.Entry(root)
            entry.pack()

            def check_number():
                number = random.randint(1, 100)
                guess = int(entry.get())
                if guess == number:
                    messagebox.showinfo("Result", "Congratulations! You guessed the number.")
                else:
                    messagebox.showinfo("Result", f"Sorry, the number was {number}.")
            tk.Button(root, text="Check", command=check_number).pack()
tk.Label(root, text="Choose Rock, Paper, or Scissors").pack()
tk.Button(root, text="Rock", command=lambda: play_rps("Rock")).pack()
tk.Button(root, text="Paper", command=lambda: play_rps("Paper")).pack()
tk.Button(root, text="Scissors", command=lambda: play_rps("Scissors")).pack()

root.mainloop()
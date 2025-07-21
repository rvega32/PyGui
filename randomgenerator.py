import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Game Hub")
root.geometry("500x400")
root.configure(bg="#f2f2f2") 

rock_img = tk.PhotoImage(file="rock.png")
paper_img = tk.PhotoImage(file="paper.png")
scissors_img = tk.PhotoImage(file="scissors.png")

def switch_to_rps():
    clear_screen()
    start_rps_game()

def switch_to_number_game():
    clear_screen()
    start_number_game()

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def start_rps_game():
    tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"), fg="#333", bg="#f2f2f2").pack(pady=10)

    def play_rps(user_choice):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)

        result = ""
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win!"
        else:
            result = "Computer Wins!"

        messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

    frame = tk.Frame(root, bg="#f2f2f2")
    frame.pack(pady=20)

    tk.Button(frame, image=rock_img, command=lambda: play_rps("Rock"), bg="#f2f2f2").grid(row=0, column=0, padx=10)
    tk.Button(frame, image=paper_img, command=lambda: play_rps("Paper"), bg="#f2f2f2").grid(row=0, column=1, padx=10)
    tk.Button(frame, image=scissors_img, command=lambda: play_rps("Scissors"), bg="#f2f2f2").grid(row=0, column=2, padx=10)

    tk.Button(root, text="Switch to Number Guessing Game", command=switch_to_number_game,
              bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=20)

def start_number_game():
    tk.Label(root, text="Number Guessing Game", font=("Arial", 20, "bold"), fg="#333", bg="#f2f2f2").pack(pady=10)
    tk.Label(root, text="Guess a number between 1 and 100", bg="#f2f2f2").pack()

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def check_guess():
        try:
            guess = int(entry.get())
            if guess < 1 or guess > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Enter a number between 1 and 100")
            return

        number = random.randint(1, 100)
        if guess == number:
            messagebox.showinfo("Result", f"Correct! The number was {number}")
        else:
            messagebox.showinfo("Result", f"Wrong! The number was {number}")

    tk.Button(root, text="Guess", command=check_guess, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="Back to Rock Paper Scissors", command=switch_to_rps,
              bg="#FF5722", fg="white", font=("Arial", 12)).pack(pady=20)

switch_to_rps()
root.mainloop()

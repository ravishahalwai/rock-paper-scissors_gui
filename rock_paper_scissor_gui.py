import tkinter as tk
import random
from tkinter import messagebox
try:
    from playsound import playsound
    SOUND = True
except ImportError:
    SOUND = False

# Main window setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x500")
root.configure(bg="#1f1f2e")

# Global variables
choices = ['Rock', 'Paper', 'Scissors']
player_score = 0
computer_score = 0

# Play sound if available
def play_sound():
    if SOUND:
        playsound('click.wav', block=False)  # You can use any short .wav file

# Logic to determine winner
def determine_winner(player, computer):
    global player_score, computer_score

    result = ""
    if player == computer:
        result = "It's a Draw!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        result = "You Win!"
        player_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    update_result_label(player, computer, result)

# Update display
def update_result_label(player, computer, result):
    result_label.config(text=f"You: {player}\nComputer: {computer}\n\n{result}",
                        fg="white", bg="#1f1f2e", font=("Arial", 16))
    score_label.config(text=f"Score - You: {player_score} | Computer: {computer_score}",
                       fg="white", bg="#1f1f2e", font=("Arial", 12))

# Player makes a choice
def make_choice(player_choice):
    play_sound()
    computer_choice = random.choice(choices)
    determine_winner(player_choice, computer_choice)

# GUI Elements
title = tk.Label(root, text="Rock Paper Scissors", fg="cyan", bg="#1f1f2e", font=("Helvetica", 20, "bold"))
title.pack(pady=20)

frame = tk.Frame(root, bg="#1f1f2e")
frame.pack(pady=20)

# Buttons
rock_btn = tk.Button(frame, text="Rock", width=10, height=2, bg="tomato", fg="white", font=("Arial", 12),
                     command=lambda: make_choice("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(frame, text="Paper", width=10, height=2, bg="skyblue", fg="white", font=("Arial", 12),
                      command=lambda: make_choice("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(frame, text="Scissors", width=10, height=2, bg="limegreen", fg="white", font=("Arial", 12),
                         command=lambda: make_choice("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", bg="#1f1f2e")
result_label.pack(pady=30)

# Score Label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", bg="#1f1f2e", fg="white", font=("Arial", 12))
score_label.pack()

# Exit button
exit_btn = tk.Button(root, text="Exit", command=root.quit, bg="#ff5555", fg="white", font=("Arial", 12))
exit_btn.pack(pady=20)

root.mainloop()

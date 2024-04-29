import tkinter as tk
from tkinter import Canvas, messagebox, simpledialog
import random

# Global variables
tickets = 0

# Function for the click game
def launch_click_game():
    def object_clicked(event, obj_color):
        global tickets
        if obj_color == 'blue':
            score[0] += 1
            tickets += 1
        elif obj_color == 'red':
            score[0] -= 1
        score_label.config(text=f"Score: {score[0]}", fg='#00ff00')  # Adjust text color
        canvas.delete("object")

    def show_object():
        canvas.delete("object")
        obj_color = random.choice(['blue', 'red'])
        x1, y1 = random.randint(10, 290), random.randint(10, 290)
        canvas.create_oval(x1, y1, x1+30, y1+30, fill=obj_color, tags="object")
        canvas.tag_bind("object", '<Button-1>', lambda event: object_clicked(event, obj_color))
        
        # Schedule next object appearance
        delay = random.randint(500, 1000)  # Time in milliseconds
        click_game_window.after(delay, show_object)

    # Initialize score
    score = [0]

    # Create the game window
    click_game_window = tk.Toplevel()
    click_game_window.title("Click Game")
    click_game_window.geometry("300x350")

    # Score label
    score_label = tk.Label(click_game_window, text="Score: 0", font=("Helvetica", 14), fg='#00ff00')  # Adjust text color
    score_label.pack()

    # Canvas
    canvas = tk.Canvas(click_game_window, width=300, height=300, bg='#000')  # Adjust background color
    canvas.pack()

    show_object()  # Start showing objects

# Function to update tickets
def cash_out():
    global tickets
    messagebox.showinfo("Cash Out", f"You have cashed out {tickets} tickets!")
    tickets = 0

# Function for the letter guessing game
def letter_guessing_game(score_label):
    letter_range = 'abcdef'
    target_letter = random.choice(letter_range)
    score = [0]  # Initialize score

    while True:
        user_guess = simpledialog.askstring("Letter Guessing Game", f"Guess a letter between {letter_range}:")
        
        if user_guess is None:
            messagebox.showinfo("Letter Guessing Game", "Game canceled.")
            break

        if not user_guess or len(user_guess) != 1 or not user_guess.isalpha() or user_guess not in letter_range:
            messagebox.showwarning("Invalid Input", f"Please enter a valid single letter between {letter_range}.")
            continue

        if user_guess == target_letter:
            messagebox.showinfo("Letter Guessing Game", "Congratulations! You guessed the letter.")
            break
        elif user_guess < target_letter:
            messagebox.showinfo("Letter Guessing Game", "Too low! Try again.")
        else:
            messagebox.showinfo("Letter Guessing Game", "Too high! Try again.")
        score[0] += 1
        score_label.config(text=f"Score: {score[0]}", fg='#00ff00')  # Adjust text color

# Function for the dice guessing game
def dice_guessing_game(score_label):
    target_number = random.randint(1, 6)
    score = [0]  # Initialize score

    while True:
        user_guess = simpledialog.askinteger("Dice Guessing Game", "Guess a number between 1 and 6:")
        
        if user_guess is None:
            messagebox.showinfo("Dice Guessing Game", "Game canceled.")
            break

        if not user_guess or user_guess < 1 or user_guess > 6:
            messagebox.showwarning("Invalid Input", "Please enter a valid number between 1 and 6.")
            continue

        if user_guess == target_number:
            messagebox.showinfo("Dice Guessing Game", "Congratulations! You guessed the correct number.")
            break
        elif user_guess < target_number:
            messagebox.showinfo("Dice Guessing Game", "Too low! Try again.")
        else:
            messagebox.showinfo("Dice Guessing Game", "Too high! Try again.")
        score[0] += 1
        score_label.config(text=f"Score: {score[0]}", fg='#00ff00')  # Adjust text color

# Main application window
arcade_window = tk.Tk()
arcade_window.title("Arcade UI")
arcade_window.config(bg="#000")  # Adjust background color

# Buttons for different games
btn_game1 = tk.Button(arcade_window, text="Play Click Game", command=launch_click_game, bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game1.pack(pady=10)

# Create score labels for games
score_label_letter = tk.Label(arcade_window, text="Score: 0", font=("Helvetica", 14), fg='#00ff00')  # Adjust text color
score_label_dice = tk.Label(arcade_window, text="Score: 0", font=("Helvetica", 14), fg='#00ff00')  # Adjust text color

btn_game2 = tk.Button(arcade_window, text="Start Letter Guessing Game", command=lambda: letter_guessing_game(score_label_letter), bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game2.pack(pady=10)

btn_game3 = tk.Button(arcade_window, text="Start Dice Guessing Game", command=lambda: dice_guessing_game(score_label_dice), bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game3.pack(pady=10)

# Cash out button
btn_cash_out = tk.Button(arcade_window, text="Cash Out Tickets", command=cash_out, bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_cash_out.pack(pady=10)

arcade_window.mainloop()

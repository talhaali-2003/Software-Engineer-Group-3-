import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound effects
click_sound = pygame.mixer.Sound("Group Project 4/click_sound.wav")
win_sound = pygame.mixer.Sound("Group Project 4/win_sound.wav")
lose_sound = pygame.mixer.Sound("Group Project 4/lose_sound.wav")

# Global variables
tickets = 0

# Function to change button color on hover
def on_enter(event):
    event.widget.config(bg="#00cc00", fg="#ffffff")  # Change background and text color on hover

# Function to reset button color when mouse leaves
def on_leave(event):
    event.widget.config(bg="#00ff00", fg="#000000")  # Reset background and text color when mouse leaves

# Function for the click game
def launch_click_game():
    def object_clicked(event, obj_color):
        global tickets
        if obj_color == 'blue':
            score[0] += 1
            tickets += 1
            win_sound.play()  # Play win sound
        elif obj_color == 'red':
            score[0] -= 1
            lose_sound.play()  # Play lose sound
        score_label.config(text=f"Score: {score[0]}", fg='#00ff00')  # Adjust text color
        canvas.delete("object")
        click_sound.play()  # Play click sound

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
            win_sound.play()  # Play win sound
            break
        elif user_guess < target_letter:
            messagebox.showinfo("Letter Guessing Game", "Too low! Try again.")
        else:
            messagebox.showinfo("Letter Guessing Game", "Too high! Try again.")
            lose_sound.play()  # Play lose sound
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
            win_sound.play()  # Play win sound
            break
        elif user_guess < target_number:
            messagebox.showinfo("Dice Guessing Game", "Too low! Try again.")
        else:
            messagebox.showinfo("Dice Guessing Game", "Too high! Try again.")
            lose_sound.play()  # Play lose sound
        score[0] += 1
        score_label.config(text=f"Score: {score[0]}", fg='#00ff00')  # Adjust text color


# Function for the Simon game
def simon_game():
    # Define the sequences for each mode
    number_sequence = random.choices("12345", k=5)
    letter_sequence = random.choices("qwertasdfgzxcvb", k=5)

    # Choose the mode
    mode = simpledialog.askstring("Simon Game", "Choose a mode (Numbers / Letters):")

    if mode.lower() == "numbers":
        sequence = number_sequence
    elif mode.lower() == "letters":
        sequence = letter_sequence
    else:
        messagebox.showerror("Simon Game", "Invalid mode selected.")
        return

    # Display the sequence to the player
    messagebox.showinfo("Simon Game", f"Remember the sequence:\n{' '.join(sequence)}")

    # Ask the player to input the sequence
    user_input = simpledialog.askstring("Simon Game", "Enter the sequence:")

    # Check if the player's input matches the generated sequence
    if user_input == ''.join(sequence):
        messagebox.showinfo("Simon Game", "Congratulations! You remembered the sequence.")
    else:
        messagebox.showinfo("Simon Game", f"Sorry, the correct sequence was {''.join(sequence)}.")

# Main application window
arcade_window = tk.Tk()
arcade_window.title("Arcade UI")
arcade_window.config(bg="#222")  # Adjust background color

# Title label
title_label = tk.Label(arcade_window, text="Arcade Games", font=("Helvetica", 24, "bold"), fg="#00ff00", bg="#222")
title_label.pack(pady=20)

# Buttons for different games
btn_game1 = tk.Button(arcade_window, text="Play Click Game", command=launch_click_game, bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game1.pack(pady=10)
btn_game1.bind("<Enter>", on_enter)  # Bind hover event
btn_game1.bind("<Leave>", on_leave)  # Bind leave event

btn_game2 = tk.Button(arcade_window, text="Start Letter Guessing Game", command=lambda: letter_guessing_game(score_label_letter), bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game2.pack(pady=10)
btn_game2.bind("<Enter>", on_enter)  # Bind hover event
btn_game2.bind("<Leave>", on_leave)  # Bind leave event

btn_game3 = tk.Button(arcade_window, text="Start Dice Guessing Game", command=lambda: dice_guessing_game(score_label_dice), bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game3.pack(pady=10)
btn_game3.bind("<Enter>", on_enter)  # Bind hover event
btn_game3.bind("<Leave>", on_leave)  # Bind leave event

btn_game4 = tk.Button(arcade_window, text="Play Simon Game", command=simon_game, bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_game4.pack(pady=10)
btn_game4.bind("<Enter>", on_enter)  # Bind hover event
btn_game4.bind("<Leave>", on_leave)  # Bind leave event

# Create score labels for games
score_label_letter = tk.Label(arcade_window, text="Score: 0", font=("Helvetica", 14), fg='#00ff00')  # Adjust text color
score_label_dice = tk.Label(arcade_window, text="Score: 0", font=("Helvetica", 14), fg='#00ff00')  # Adjust text color

# Cash out button
btn_cash_out = tk.Button(arcade_window, text="Cash Out Tickets", command=cash_out, bg='#00ff00', fg='#000000', font=("Helvetica", 16), width=25, height=2)
btn_cash_out.pack(pady=10)
btn_cash_out.bind("<Enter>", on_enter)  # Bind hover event
btn_cash_out.bind("<Leave>", on_leave)  # Bind leave event

arcade_window.mainloop()

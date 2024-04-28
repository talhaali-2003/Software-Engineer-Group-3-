import tkinter as tk
from tkinter import Canvas, messagebox, PhotoImage
import random
import time     


import tkinter as tk
from tkinter import messagebox
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
        score_label.config(text=f"Score: {score[0]}")
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
    score_label = tk.Label(click_game_window, text="Score: 0", font=("Helvetica", 14))
    score_label.pack()

    # Canvas
    canvas = tk.Canvas(click_game_window, width=300, height=300, bg='white')
    canvas.pack()

    show_object()  # Start showing objects

# Function to update tickets
def cash_out():
    global tickets
    messagebox.showinfo("Cash Out", f"You have cashed out {tickets} tickets!")
    tickets = 0

# Main application window
arcade_window = tk.Tk()
arcade_window.title("Arcade UI")
arcade_window.config(bg="#333333")

# Customize button appearance
btn_style = {"bg": "#555555", "fg": "#ffffff", "font": ("Helvetica", 16), "width": 25, "height": 2}

# Buttons for different games
btn_game1 = tk.Button(arcade_window, text="Play Click Game", command=launch_click_game, **btn_style)
btn_game1.pack(pady=10)

# Cash out button
btn_cash_out = tk.Button(arcade_window, text="Cash Out Tickets", command=cash_out, **btn_style)
btn_cash_out.pack(pady=10)

arcade_window.mainloop()

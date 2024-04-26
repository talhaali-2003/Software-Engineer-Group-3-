import tkinter as tk
from tkinter import Canvas, messagebox, PhotoImage
import random
import time     


def launch_click_game():
    def object_clicked(event, obj_color):
        if obj_color == 'blue':
            score[0] += 1
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

# Main application window
arcade_window = tk.Tk()
arcade_window.title("Arcade UI")
arcade_window.config(bg="#333333")

# Customize button appearance
btn_style = {"bg": "#555555", "fg": "#ffffff", "font": ("Helvetica", 16), "width": 25, "height": 2}

# Button to play the "click game"
btn_game1 = tk.Button(arcade_window, text="Play Click Game", command=launch_click_game, **btn_style)
btn_game1.pack(pady=20)

arcade_window.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import turtle
import random
from datetime import datetime

# Data storage
expenses = []

# Add an expense
def add_expense():
    date_str = date_var.get()
    amount_str = amount_var.get()
    category = category_var.get()
    
    # Validate input
    try:
        # Check if any field is empty
        if not date_str or not amount_str or not category:
            raise ValueError("All fields must be filled out")
        
        # Validate and convert date
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Validate and convert amount
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        expenses.append((date, category, amount))
        amount_entry.delete(0, tk.END)  # Clear the entry
        date_entry.delete(0, tk.END)  # Clear the date entry
        print(f"Added: {date.strftime('%Y-%m-%d')} {category} - ${amount}")
    except ValueError as e:
        messagebox.showwarning("Validation Error", str(e))

# Draw the chart
def draw_chart():
    chart_type = chart_type_var.get()
    
    if chart_type == 'Bar Chart':
        draw_bar_chart()
    elif chart_type == 'Line Graph':
        draw_line_graph()
    else:
        messagebox.showerror("Error", "Please select a valid chart type")

from collections import defaultdict
import calendar

def draw_bar_chart():
    if not expenses:
        messagebox.showinfo("Info", "No expenses to display.")
        return
    
    # Aggregate expenses by month
    totals_by_month = defaultdict(float)
    for date, category, amount in expenses:
        month = date.strftime("%Y-%m")  # Format as 'YYYY-MM'
        totals_by_month[month] += amount

    # Sort totals by month from lowest to highest
    sorted_months = sorted(totals_by_month.keys(), key=lambda x: totals_by_month[x])

    # Setup Turtle
    turtle.clearscreen()
    turtle.title("Monthly Expense Chart")
    turtle.bgcolor("white")
    turtle.setup(width=1000, height=600)
    turtle.penup()
    turtle.goto(-450, -100)

    max_height = max(totals_by_month.values())
    scaling_factor = 150 / max_height

    bar_width = 40
    spacing = 50

    for month in sorted_months:
        amount = totals_by_month[month]
        turtle.fillcolor(random.choice(['red', 'green', 'blue', 'yellow', 'purple']))
        turtle.begin_fill()

        # Draw bar
        turtle.forward(bar_width)
        turtle.left(90)
        turtle.forward(amount * scaling_factor)
        turtle.left(90)
        turtle.forward(bar_width)
        turtle.left(90)
        turtle.forward(amount * scaling_factor)
        turtle.left(90)

        turtle.end_fill()

        # Label for the month and amount
        turtle.penup()
        turtle.forward(bar_width / 2)
        turtle.left(90)
        turtle.forward(amount * scaling_factor + 20)
        month_name = calendar.month_abbr[int(month.split("-")[1])]  # Convert "YYYY-MM" to abbreviated month name
        turtle.write(f"{month_name}\n${amount:.2f}", align="center")
        turtle.backward(amount * scaling_factor + 20)
        turtle.right(90)
        turtle.backward(bar_width / 2)

        # Move to next bar position
        turtle.forward(bar_width + spacing)
        turtle.pendown()

    turtle.hideturtle()
    turtle.done()


def draw_line_graph():
    if not expenses:
        messagebox.showinfo("Info", "No expenses to display.")
        return
    
    # Placeholder for the line graph drawing code
    print("Drawing line graph...")  # Replace with actual drawing code

# Tkinter GUI setup
# Adjustments for window size and layout
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("400x200")  # Increased window size for more space

# Configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)  # Give more space to the entry fields

# Adding more category options
categories = ["Food", "Transport", "Entertainment", "Utilities", "Shopping", "Healthcare", "Travel", "Education", "Miscellaneous"]

# Date entry
date_var = tk.StringVar()
date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)
date_entry = ttk.Entry(root, textvariable=date_var)
date_entry.grid(column=1, row=0, sticky=tk.EW, padx=10, pady=5)

chart_type_var = tk.StringVar()
chart_type_label = ttk.Label(root, text="Chart Type:")
chart_type_label.grid(column=0, row=4, sticky=tk.W, padx=10, pady=5)
chart_type_dropdown = ttk.Combobox(root, textvariable=chart_type_var, values=['Bar Chart', 'Line Graph'])
chart_type_dropdown.grid(column=1, row=4, sticky=tk.EW, padx=10, pady=5)
chart_type_dropdown.current(0) 

# Amount entry
amount_var = tk.StringVar()
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)
amount_entry = ttk.Entry(root, textvariable=amount_var)
amount_entry.grid(column=1, row=1, sticky=tk.EW, padx=10, pady=5)

# Category selection
category_var = tk.StringVar()
category_label = ttk.Label(root, text="Category:")
category_label.grid(column=0, row=2, sticky=tk.W, padx=10, pady=5)
category_entry = ttk.Combobox(root, textvariable=category_var, values=categories)
category_entry.grid(column=1, row=2, sticky=tk.EW, padx=10, pady=5)
category_entry.current(0)  # Default selection

# Adjusting button layout and adding space between buttons
add_button = ttk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
draw_button = ttk.Button(root, text="Draw Chart", command=draw_chart)
draw_button.grid(column=1, row=3, padx=10, pady=10, sticky=tk.E)

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class PizzaOrderingSystem:
    def __init__(self, root, inventory=None):
        self.root = root
        self.root.title("Pizza Ordering and Inventory Management System")
        self.root.configure(bg="#FFD166")  # Set background color
        
        # Define pizza sizes, crusts, and toppings
        self.sizes = ["Small", "Medium", "Large"]
        self.crusts = ["Thin Crust", "Regular Crust", "Thick Crust"]
        self.toppings = ["Cheese", "Tomatoes", "Basil", "Pepperoni", "Peppers", "Olives", "Onions", "Mushrooms", "Ham", "Pineapple"]
        
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = {
                        "Margherita": {"Cheese": 2, "Tomatoes": 1, "Basil": 1},
                        "Pepperoni": {"Cheese": 2, "Pepperoni": 3},
                        "Vegetarian": {"Cheese": 2, "Peppers": 1, "Olives": 1, "Onions": 1, "Mushrooms": 1},
                        "Hawaiian": {"Cheese": 2, "Ham": 2, "Pineapple": 1}
                    }        
        
        # Initialize order variables
        self.selected_pizza = tk.StringVar(root)
        self.selected_pizza.set("Select Pizza")
        self.selected_size = tk.StringVar(root)
        self.selected_size.set(self.sizes[0])  # Default size
        self.selected_crust = tk.StringVar(root)
        self.selected_crust.set(self.crusts[0])  # Default crust
        self.selected_toppings = [tk.BooleanVar(root, value=False) for _ in range(len(self.toppings))]
        self.quantity = tk.StringVar(root)
        self.quantity.set("1")
        self.customer_name = tk.StringVar(root)
        self.customer_phone = tk.StringVar(root)
        
        # Load orders from JSON file
        self.orders = []
        try:
            with open("orders.json", "r") as file:
                self.orders = json.load(file)
        except FileNotFoundError:
            pass
        # Load and display the pizza image
        self.pizza_image = tk.PhotoImage(file="Group Project 3/pizza_gif.gif")
        self.pizza_image_label = tk.Label(self.root, image=self.pizza_image)
        self.pizza_image_label.grid(row=0, column=0, columnspan=2, pady=10)
        # Create ordering GUI
        self.create_order_gui()
        

    def create_order_gui(self):
        # Create ordering GUI
        label = tk.Label(self.root, text="Order Pizza", bg="#FFD166", fg="#333333", font=("Arial", 16, "bold"))
        label.grid(row=1, column=0, columnspan=2, pady=10)  # Moved below the image
        
        pizza_label = tk.Label(self.root, text="Pizza:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        pizza_label.grid(row=2, column=0, sticky="w")
        pizza_dropdown = tk.OptionMenu(self.root, self.selected_pizza, *self.inventory.keys())
        pizza_dropdown.config(bg="#FFA500", fg="#333333", font=("Arial", 12))
        pizza_dropdown.grid(row=2, column=1)
        
        size_label = tk.Label(self.root, text="Size:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        size_label.grid(row=3, column=0, sticky="w")
        size_dropdown = tk.OptionMenu(self.root, self.selected_size, *self.sizes)
        size_dropdown.config(bg="#FFA500", fg="#333333", font=("Arial", 12))
        size_dropdown.grid(row=3, column=1)
        
        crust_label = tk.Label(self.root, text="Crust:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        crust_label.grid(row=4, column=0, sticky="w")
        crust_dropdown = tk.OptionMenu(self.root, self.selected_crust, *self.crusts)
        crust_dropdown.config(bg="#FFA500", fg="#333333", font=("Arial", 12))
        crust_dropdown.grid(row=4, column=1)
        
        toppings_label = tk.Label(self.root, text="Toppings:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        toppings_label.grid(row=5, column=0, sticky="w")
        for idx, topping in enumerate(self.toppings):
            topping_frame = tk.Frame(self.root, bg="#FFD166")
            topping_frame.grid(row=5+idx, column=1, sticky="w")
            topping_checkbox = tk.Checkbutton(topping_frame, text=topping, variable=self.selected_toppings[idx], bg="#FFD166", fg="#333333", font=("Arial", 12))
            topping_checkbox.pack(side=tk.LEFT)
            topping_image = tk.PhotoImage(file=f"Group Project 3/topping_images/{topping.lower()}.gif")
            topping_image = topping_image.subsample(5, 5)  # Resizing the image
            topping_label = tk.Label(topping_frame, image=topping_image, bg="#FFD166")
            topping_label.image = topping_image
            topping_label.pack(side=tk.LEFT)
        
        quantity_label = tk.Label(self.root, text="Quantity:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        quantity_label.grid(row=6+len(self.toppings), column=0, sticky="w")
        quantity_entry = tk.Entry(self.root, textvariable=self.quantity)
        quantity_entry.grid(row=6+len(self.toppings), column=1)
        
        customer_name_label = tk.Label(self.root, text="Customer Name:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        customer_name_label.grid(row=7+len(self.toppings), column=0, sticky="w")
        customer_name_entry = tk.Entry(self.root, textvariable=self.customer_name)
        customer_name_entry.grid(row=7+len(self.toppings), column=1)
        
        customer_phone_label = tk.Label(self.root, text="Customer Phone:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        customer_phone_label.grid(row=8+len(self.toppings), column=0, sticky="w")
        customer_phone_entry = tk.Entry(self.root, textvariable=self.customer_phone)
        customer_phone_entry.grid(row=8+len(self.toppings), column=1)
        
        order_button = tk.Button(self.root, text="Place Order", command=self.place_order, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        order_button.grid(row=9+len(self.toppings), column=0, columnspan=2, pady=10)
        
        switch_button = tk.Button(self.root, text="Switch to Inventory Management", command=self.switch_to_management, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        switch_button.grid(row=10+len(self.toppings), column=0, columnspan=2)

    def place_order(self):
        pizza = self.selected_pizza.get()
        size = self.selected_size.get()
        crust = self.selected_crust.get()
        quantity = self.quantity.get()
        customer_name = self.customer_name.get()
        customer_phone = self.customer_phone.get()

        # Validate user input
        if pizza == "Select Pizza" or pizza not in self.inventory:
            tk.messagebox.showerror("Error", "Please select a valid pizza.")
            return

        if size not in self.sizes:
            tk.messagebox.showerror("Error", "Please select a valid size.")
            return

        if crust not in self.crusts:
            tk.messagebox.showerror("Error", "Please select a valid crust.")
            return

        if not customer_name:
            tk.messagebox.showerror("Error", "Please enter customer name.")
            return

        if not customer_phone:
            tk.messagebox.showerror("Error", "Please enter customer phone number.")
            return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Error", "Quantity must be a positive integer.")
            return

        # Check if inventory is sufficient for each ingredient needed for the pizza
        sufficient_inventory = True
        for topping, amount in self.inventory[pizza].items():
            if self.inventory[pizza][topping] < quantity * amount:
                sufficient_inventory = False
                break

        if not sufficient_inventory:
            tk.messagebox.showerror("Error", "Insufficient ingredients for the pizza. Please adjust your order!")
            return
        else:
            # Deduct ingredients from inventory
            for topping, amount in self.inventory[pizza].items():
                self.inventory[pizza][topping] -= quantity * amount

            # Create and save the order
            order = {
                "pizza": pizza,
                "size": size,
                "crust": crust,
                "quantity": quantity,
                "customer_name": customer_name,
                "customer_phone": customer_phone,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.orders.append(order)
            with open("orders.json", "w") as file:
                json.dump(self.orders, file, indent=4)

            tk.messagebox.showinfo("Order Placed", f"{quantity} {size} {crust} {pizza} pizza(s) ordered for {customer_name}!")

    def switch_to_management(self):
        self.root.destroy()
        root = tk.Tk()
        management_system = InventoryManagementSystem(root, self.inventory)
        root.mainloop()


class InventoryManagementSystem:
    def __init__(self, root, inventory):
        self.root = root
        self.root.title("Pizza Ordering and Inventory Management System")
        self.root.configure(bg="#FFD166")  # Set background color

        # Set up password protection
        self.admin_password = "pizzahutsucks"

        # Create password entry and button
        self.password_label = tk.Label(self.root, text="Enter Admin Password:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        self.password_label.grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=0, column=1, pady=(10, 0))
        self.password_button = tk.Button(self.root, text="Submit", command=self.check_password, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        self.password_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Initialize inventory
        self.inventory = inventory

        # Load orders from JSON file
        self.orders = []
        try:
            with open("orders.json", "r") as file:
                self.orders = json.load(file)
        except FileNotFoundError:
            pass

    def check_password(self):
        entered_password = self.password_entry.get()
        if entered_password == self.admin_password:
            self.show_management_gui()
        else:
            messagebox.showerror("Error", "Invalid password. Access denied.")

    def show_management_gui(self):
        self.password_label.grid_forget()
        self.password_entry.grid_forget()
        self.password_button.grid_forget()

        # Create management GUI
        self.create_management_gui()

    def create_management_gui(self):
        label = tk.Label(self.root, text="Inventory Management", bg="#FFD166", fg="#333333", font=("Arial", 16, "bold"))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        inventory_label = tk.Label(self.root, text="Inventory:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        inventory_label.grid(row=1, column=0, sticky="w")

        self.inventory_listbox = tk.Listbox(self.root, width=50, height=15)  # Enlarged the listbox
        self.inventory_listbox.grid(row=1, column=1)
        self.update_inventory_list()

        revenue_label = tk.Label(self.root, text="Revenue:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        revenue_label.grid(row=2, column=0, sticky="w")

        self.revenue_label = tk.Label(self.root, text="$0", bg="#FFD166", fg="#333333", font=("Arial", 12))
        self.revenue_label.grid(row=2, column=1)
        self.calculate_revenue()

        switch_button = tk.Button(self.root, text="Switch to Pizza Ordering", command=self.switch_to_ordering, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        switch_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.update_inventory_list()

        self.timesheet_system = TimesheetSystem(self.root)

        search_label = tk.Label(self.root, text="Search Orders by Full Name:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        search_label.grid(row=10, column=0, sticky="w", pady=(10, 0))
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=10, column=1, pady=(10, 0))

        search_button = tk.Button(self.root, text="Search", command=self.search_orders, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        search_button.grid(row=11, column=0, columnspan=2)

        self.search_results_listbox = tk.Listbox(self.root, width=50, height=10)
        self.search_results_listbox.grid(row=12, column=0, columnspan=2)

    def update_inventory_list(self):
        self.inventory_listbox.delete(0, tk.END)
        for pizza, ingredients in self.inventory.items():
            self.inventory_listbox.insert(tk.END, f"{pizza}: {', '.join([f'{ingredient}: {quantity}' for ingredient, quantity in ingredients.items()])}")

    def calculate_revenue(self):
        revenue = 0
        for order in self.orders:
            revenue += 10 * order["quantity"]  # Assuming each pizza costs $10
        self.revenue_label.config(text=f"${revenue}")

    def switch_to_ordering(self):
        self.root.destroy()
        root = tk.Tk()
        pizza_ordering_system = PizzaOrderingSystem(root, self.inventory)
        root.mainloop()

    def search_orders(self):
        search_query = self.search_entry.get().lower()
        self.search_results_listbox.delete(0, tk.END)
        for order in self.orders:
            if search_query in order["customer_name"].lower():
                self.search_results_listbox.insert(tk.END, f"Name: {order['customer_name']}, Phone: {order['customer_phone']}, Pizza: {order['pizza']}, Size: {order['size']}, Crust: {order['crust']}, Quantity: {order['quantity']}, Timestamp: {order['timestamp']}")


class TimesheetSystem:
    def __init__(self, root):
        self.root = root
        self.timeslots = {
            "6 AM - 10 AM": [],
            "10 AM - 2 PM": [],
            "2 PM - 6 PM": [],
            "6 PM - 10 PM": [],
        }

        # Preset employees
        self.employees = ["Alice", "Bob", "Charlie", "Dana", "Evan"]
        
        # Create timesheet GUI below the management GUI
        self.create_timesheet_gui()

    def create_timesheet_gui(self):
        label = tk.Label(self.root, text="Employee Timesheet", bg="#FFD166", fg="#333333", font=("Arial", 16, "bold"))
        label.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        
        self.timeslot_listbox = tk.Listbox(self.root, width=50, height=10)  # Enlarged the listbox
        self.timeslot_listbox.grid(row=5, column=0, columnspan=2)
        self.update_timeslot_list()
        
        add_employee_label = tk.Label(self.root, text="Add/Remove Employee:", bg="#FFD166", fg="#333333", font=("Arial", 12, "bold"))
        add_employee_label.grid(row=6, column=0, sticky="w")
        self.employee_name_entry = tk.Entry(self.root)
        self.employee_name_entry.grid(row=6, column=1)

        self.timeslot_var = tk.StringVar(self.root)
        self.timeslot_var.set("Select Timeslot")
        timeslot_dropdown = tk.OptionMenu(self.root, self.timeslot_var, *self.timeslots.keys())
        timeslot_dropdown.grid(row=7, column=0, columnspan=2, pady=(10, 0), sticky="nsew")
        
        add_button = tk.Button(self.root, text="Add Employee", command=self.add_employee_to_timeslot, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        add_button.grid(row=8, column=0, sticky="w") 

        add_button = tk.Button(self.root, text="Remove Employee", command=self.add_employee_to_timeslot, bg="#FFA500", fg="#333333", font=("Arial", 12, "bold"))
        add_button.grid(row=8, column=1, sticky="w") 


    def update_timeslot_list(self):
        self.timeslot_listbox.delete(0, tk.END)
        for timeslot, employees in self.timeslots.items():
            self.timeslot_listbox.insert(tk.END, f"{timeslot}: {', '.join(employees) if employees else 'Empty'}")

    def add_employee_to_timeslot(self):
        employee = self.employee_name_entry.get()
        if not all(x.isalpha() or x.isspace() for x in employee):
            messagebox.showerror("Error", "Employee name must contain only letters.")
            return
        timeslot = self.timeslot_var.get()
        if timeslot not in self.timeslots or employee == "":
            messagebox.showerror("Error", "Please select a valid timeslot and enter employee name.")
            return
        if employee in self.timeslots[timeslot]:
            messagebox.showerror("Error", "Employee already assigned to this timeslot.")
            return
        self.timeslots[timeslot].append(employee)
        self.update_timeslot_list()

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    pizza_ordering_system = PizzaOrderingSystem(root)
    root.mainloop()

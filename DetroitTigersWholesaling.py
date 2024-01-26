#import the proper modules
import tkinter
import os
import csv
from tkinter import ttk
import tkinter.messagebox

#function for adding the inputs to a .csv file
def add_data():
    # Company & Product info
    companyName = company_name_entry.get()
    productID = product_id_entry.get()

    if companyName and productID:
        # Product Information
        productType = product_type_combobox.get()
        productQuantity = quantity_spinbox.get()
        productName = product_name_entry.get()

        # Check if the file is empty (no headers)
        is_empty = os.stat('DetroitTigersWholesaling.csv').st_size == 0

        # Open the CSV file in append mode
        with open('DetroitTigersWholesaling.csv', 'w', newline='') as DTW:
            writer = csv.writer(DTW, delimiter=',')

            # Write headers if the file is empty
            if is_empty:
                writer.writerow(['Company Name', 'Product ID', 'Product Name', 'Product Type', 'Product Quantity'])

            # Write the data to the CSV file
            writer.writerow([companyName, productID, productName, productType, productQuantity])

        # Display success message
        tkinter.messagebox.showinfo(title="Success", message="Data successfully added!")

        # Clear the entry fields after adding data
        company_name_entry.delete(0, 'end')
        product_id_entry.delete(0, 'end')
        product_type_combobox.set('')  # Reset the combobox
        quantity_spinbox.delete(0, 'end')
        product_name_entry.delete(0, 'end')

    else:
        # Display error message if fields are not filled
        tkinter.messagebox.showwarning(title="Error", message="YOU DID NOT FILL ALL THE FIELDS.")
# Creating a GUI window
window = tkinter.Tk()
window.title("Detroit Tiger Wholesaling Form")

# Creating a frame that will sit in the window
frame = tkinter.Frame(window)
frame.pack()

# Creating a labeled frame for Company & Product Information
company_info_frame = tkinter.LabelFrame(frame, text="Company & Product Information")
company_info_frame.grid(row= 0, column=0, padx=20, pady=10)

# Creating a label and entry for Company Name
company_name_label = tkinter.Label(company_info_frame, text="Company Name")
company_name_label.grid(row=0, column=0)

company_name_entry = tkinter.Entry(company_info_frame)
company_name_entry.grid(row=1, column=0)

# Creating a label and entry for Product ID
product_id_label = tkinter.Label(company_info_frame, text="Product ID")
product_id_label.grid(row=0, column=1)

product_id_entry = tkinter.Entry(company_info_frame)
product_id_entry.grid(row=1, column=1)

# Creating a label and entry for Product Name
product_name_label = tkinter.Label(company_info_frame, text="Product Name")
product_name_label.grid(row=0, column=2)

product_name_entry = tkinter.Entry(company_info_frame)
product_name_entry.grid(row=1, column=2)

# Creating a label and combobox for Product Type
product_type_label = tkinter.Label(company_info_frame, text="Product Type")
product_type_combobox = ttk.Combobox(company_info_frame, values=["Electronics", "Clothing", "Food", "Entertainment", "Tobacco"])
product_type_label.grid(row=2, column=0)
product_type_combobox.grid(row=3, column=0)

# Creating a label and spinbox for Quantity
quantity_label = tkinter.Label(company_info_frame, text="Quantity(MAX 20)")
quantity_spinbox = tkinter.Spinbox(company_info_frame, from_=0, to=20)
quantity_label.grid(row=2, column=1)
quantity_spinbox.grid(row=3, column=1)

# Adjusting the layout for all widgets in company_info_frame
for widget in company_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button for adding data
button = tkinter.Button(frame, text="Add Data", command= add_data)
button.grid(row=3, column=0, sticky="news", padx=0, pady=5)

#Closing Main Loop
window.mainloop()

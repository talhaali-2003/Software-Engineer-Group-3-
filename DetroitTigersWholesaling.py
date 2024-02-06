#import the proper modules
import tkinter
import os
import csv
from tkinter import ttk
import tkinter.messagebox

def is_valid_input(input_str):
    # Define allowed characters, adjust according to your needs
    allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
    return all(char in allowed_chars for char in input_str)

def add_data():
    # Company & Product info
    companyName = company_name_entry.get()
    productID = product_id_entry.get()
    productType = product_type_combobox.get()
    productQuantity = quantity_spinbox.get()
    productName = product_name_entry.get()

    # Validate inputs for foreign characters
    if not all(is_valid_input(field) for field in [companyName, productID, productName, productQuantity]):
        # Display error message
        tkinter.messagebox.showwarning(title="Error", message="Foreign characters detected. Please use only standard alphanumeric characters.")
        # Clear the entry fields
        company_name_entry.delete(0, 'end')
        product_id_entry.delete(0, 'end')
        product_type_combobox.set('')  # Reset the combobox
        quantity_spinbox.delete(0, 'end')
        product_name_entry.delete(0, 'end')
        return  # Exit the function

    if companyName and productID and productName and productType and productQuantity:
        # Check if the file is empty (no headers)
        is_empty = os.stat('DetroitTigersWholesaling.csv').st_size == 0

        # Open the CSV file in append mode
        with open('DetroitTigersWholesaling.csv', 'a', newline='', encoding='utf-8') as dtw:
            writer = csv.writer(dtw, delimiter=',')
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
        # Display error message if fields are not filled correctly
        tkinter.messagebox.showwarning(title="Error", message="FIELDS ARE NOT FILLED CORRECTLY OR AT ALL.")
#function for searching the inputs to a .csv file
def search_data():
    # Product ID info
    productID = product_id_search_entry.get()

    if productID:
        with open('DetroitTigersWholesaling.csv', 'r') as search_dtw:
            reader = csv.DictReader(search_dtw)
            found_flag = False

            for line in reader:
                if(line['Product ID'] == productID):
                    print(line['Product Name'] + " is in inventory with a quantity of " + line['Product Quantity'])
                    found_flag = True
                    tkinter.messagebox.showinfo(title="Success", message="Data successfully Found!")

            if (found_flag ==  False):
                print("Product is not in inventory")
                tkinter.messagebox.showinfo(title="Not Found", message="Product ID not found")

        # Clear the entry fields after searching data
        product_id_search_entry.delete(0, 'end')

    else:
        # Display error message if fields are not filled
        tkinter.messagebox.showwarning(title="Error", message="YOU DID NOT FILL ALL THE FIELDS.")

#function for removing row of data from a .csv file
def remove_data():
    productID = product_id_remove_entry.get()
    lines_keep = list()

    if productID:
        with open('DetroitTigersWholesaling.csv', 'r') as remove_dtw:
            reader = csv.DictReader(remove_dtw)
            found_flag = False

            # Stores all data except removed one in a list
            for line in reader:
                lines_keep.append(line)
                if (line["Product ID"] == productID):
                        print(line["Product Name"] + " has been removed")
                        lines_keep.remove(line)
                        found_flag = True
                        tkinter.messagebox.showinfo(title="Success", message="Data successfully removed!")

            if (found_flag == False):
                    print("Product is not in inventory")
                    tkinter.messagebox.showinfo(title="Not Found", message="Product ID not found")
        
        # Rewrites .CSV from list
        with open("DetroitTigersWholesaling.csv", "w", newline='') as wrt:
            writer = csv.writer(wrt)
            writer.writerow(lines_keep[0].keys())
            for x in range(len(lines_keep)):
                writer.writerow(lines_keep[x].values())

        # Clear the entry fields after searching data
        product_id_remove_entry.delete(0, 'end')
    
    else:
        # Display error message if fields are not filled
        tkinter.messagebox.showwarning(title="Error", message="YOU DID NOT FILL ALL THE FIELDS.")

def add_Sample_Data():
    sample_Data_List = list()
    #Read sample data
    with open('DetroitTigersWholesaling Sample Data.csv', 'r') as add_Sample_Data_dtw:
            reader = csv.DictReader(add_Sample_Data_dtw)
            # Stores all data
            for line in reader:
                sample_Data_List.append(line)

    #Write sample data to main CSV       
    #Check if the file is empty (no headers)
    is_empty = os.stat('DetroitTigersWholesaling.csv').st_size == 0

    # Open the CSV file in append mode
    with open('DetroitTigersWholesaling.csv', 'a', newline='', encoding='utf-8') as dtw:
        writer = csv.writer(dtw, delimiter=',')
        # Write headers if the file is empty
        if is_empty:
            writer.writerow(['Company Name', 'Product ID', 'Product Name', 'Product Type', 'Product Quantity'])
        # Write the data to the CSV file
        for x in range(len(sample_Data_List)):
            writer.writerow(sample_Data_List[x].values())
        tkinter.messagebox.showinfo(title="Success", message="Sample Data Added!")

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
button = tkinter.Button(frame, text="Add Data", command= add_data, width = 10)
button.grid(row=1, column=0, sticky="news", padx=5, pady=5)

# Creating a labeled frame for Product Search
search_frame = tkinter.LabelFrame(frame, text="Product Search")
search_frame.grid(row= 2, column=0, padx=20, pady=10)

# Creating a label and entry for Product ID
product_id_search_label = tkinter.Label(search_frame, text="Product ID")
product_id_search_label.grid(row=2, column=0)

product_id_search_entry = tkinter.Entry(search_frame)
product_id_search_entry.grid(row=2, column=0)

# Adjusting the layout for all widgets in search_frame
for widget in search_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button for parsing through data
buttonSearch = tkinter.Button(frame, text="Search Data", command= search_data, width = 10)
buttonSearch.grid(row=3, column=0, sticky="news", padx=5, pady=5)

# Creating a labeled frame for remove data
remove_frame = tkinter.LabelFrame(frame, text="Remove Data")
remove_frame.grid(row=2, column=1, padx=20, pady=10)

# Creating a label and entry for Product ID
product_id_remove_label = tkinter.Label(remove_frame, text="Product ID")
product_id_remove_label.grid(row=2, column=0)

product_id_remove_entry = tkinter.Entry(remove_frame)
product_id_remove_entry.grid(row=2, column=0)

# Adjusting the layout for all widgets in remove_frame
for widget in remove_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button for removing data
buttonRemove = tkinter.Button(frame, text="Remove Data", command= remove_data, width = 5)
buttonRemove.grid(row=3, column=1, sticky="news", padx=3, pady=3)

# Button for adding sample data
buttonRemove = tkinter.Button(frame, text="Add Sample Data", command= add_Sample_Data, width = 5)
buttonRemove.grid(row=1, column=1, sticky="news", padx=3, pady=3)

#Closing Main Loop
window.mainloop()

class Item():

    def __init__(self, name, value):

        self._name = name
        self._value = value

        all_items.append(self)
   
    def get_name(self):
        ''' Return name of item '''

        return self._name

    def get_value(self):
        ''' Return value of item '''

        return self._value
    

def generate_items():
    ''' Import students from a csv file'''
    # Import the csv package to enable the program to work with a csv
    import csv
    # Open the csv file, call is csvfile
    with open('products.csv', newline='') as csvfile:
        # use the reader() function and put the results into a variable called filereader
        filereader = csv.reader(csvfile)
        # Loop through the csv, one row at a time
        
        for line in filereader:
            # For each row, create a new item
            
            Item(line[0], int(line[1]))

def delete_item():
    for num in listbox.curselection():
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {all_items[num].get_name()}"):
           del all_items[num]
    #delete all items from listbox then repopulate
    listbox.delete(0, END)
    listbox_fill()

def add_item():
    print("yes")

def print_selection():
    '''print out selected items'''
    for num in listbox.curselection():
        messagebox.showwarning(f"{all_items[num].get_name()}", f"{all_items[num].get_name()} costs ${all_items[num].get_value()}")

def listbox_fill():
    #Populate listbox with names of items
    for i in all_items:
        listbox.insert(END, i.get_name())
            
        

    
# Import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox

# List to store all items
all_items = []

#import the items from csv file
generate_items()

#########   SET UP GUI #########
from tkinter import *
root = Tk()
root.title("Popups demo")
root.geometry("800x500")

listbox = Listbox(root, selectmode=SINGLE)
listbox.grid(row=0, rowspan=3)
listbox_fill()

#button to enter selection
select_btn = Button(root, text="selection", command=print_selection)
select_btn.grid(row=3)
 
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=4, column=1)

#Button for deleting selected item
delete_btn = Button(root, text="Delete", command=delete_item)
delete_btn.grid(row=3, column=2)

#entry field labling
heading_lbl = Label(root, text="Add New Item")
heading_lbl.grid(row=0, column=3)

name_lbl = Label(root, text="Name")
name_lbl.grid(row=1, column=3)
name_input = Entry(root)
name_input.grid(row=1, column=4)

value_lbl = Label(root,text="Value (in $)")
value_lbl.grid(row=2, column=3)
value_input = Entry(root)
value_input.grid(row=2, column=4)

add_btn = Button(root, text="Add", command=add_item)
add_btn.grid(row=3, column=4)




#launch the program
root.mainloop()
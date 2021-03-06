class Item():

    def __init__(self, name, value):

        self._name = name
        self._value = value

        all_items.append(self)
        #appened name to item_names list
        item_names.append(name)

   
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

# function to print value
def print_value(v):

    print(v)
    item_value.set(f"${v}")

def display_selection():
    '''Get the selected item from the option menu and display details in a label'''

    #loop through all items until we find the one we selected, ad get the value
    for i in all_items:
        if i.get_name() == selected_item.get():
            value= i.get_value()
    details.set(f"{selected_item.get()} costs ${value}")
        
    
# Import tkinter
from tkinter import *
from functools import partial

# List to store all items
all_items = []
#list of all item names so we can populate the option menu
item_names = ["Select Names"]

#import the items from csv file
generate_items()

#setup GUI
from tkinter import *
root = Tk()
root.title("Option menu demo")
root.geometry("800x500")

#OPtion menu
#set up a variable to store the selection
selected_item = StringVar()
selected_item.set(item_names[0])
names_menu = OptionMenu(root, selected_item, *item_names)
names_menu.config(fg="red")
names_menu.grid(row=0)


'''ADd a button that gets the selected item, then displays the price in a label'''
#button
select_btn = Button(root, text="Select", command=display_selection)
select_btn.grid(row=0, column=1)
#Label
details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=1, column=1)


#launch the program
root.mainloop()
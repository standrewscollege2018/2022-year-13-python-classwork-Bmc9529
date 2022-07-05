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

def print_selection():
    '''print out selected items'''
    for num in listbox.curselection():
        something = True
        while something == True:
            messagebox.showinfo(f"{all_items[num].get_name()}", f"{all_items[num].get_name()} costs ${all_items[num].get_value()}")
        

    
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
listbox.grid(row=0)

#Populate listbox with names of items
for i in all_items:
    listbox.insert(END, i.get_name())

#button to enter selection
select_btn = Button(root, text="selection", command=print_selection)
select_btn.grid(row=1)

details = StringVar()
details_lbl = Label(root, textvariable=details)
details_lbl.grid(row=1, column=1)






#launch the program
root.mainloop()
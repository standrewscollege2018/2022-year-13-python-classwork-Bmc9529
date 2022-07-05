
''' This program is for demonstrating how tkinter and OO works together'''
#classes should have a capital first letter
class Item:
    '''This holds all the student objects'''
    def __init__(self, item, price):
        '''The init function is called when a new object is instantiated'''
        #sets item
        self._item = item
        self._price = price
        all_items.append(self)


    def __del__(self):
        '''This function is automatically called when the object is deleted'''
        print("Item record has permanently been deleted")

    def get_item(self):
        ''' THis function returns the name of the student object'''
        return self._item

    def get_price(self):
        '''This is a getter function that returns the phonenumber of the student object'''
        return self._price

def search_student(name):
    '''This function loops through enemy_list and displays their name and health'''
    for student in student_list:
        if name in student.get_name():
            print("="*30)
            print(f"Name: {student.get_name()}\nAge: {student.get_age()}\nPhone Number: {student.get_phonenumber()}\nEnrollment status: {student.get_enrollment()}\nClasses: {student.get_classes()}")
            print("="*30)
            print("")

def generate_items():
    '''Import items from a csv file'''
    #import the scv package to enable the program to work with a csv
    import csv
    #open the csv file, call is csvfile
    with open("products.csv", newline='') as csvfile:
        #use the reader() function and put the results intp a vairable called filereader
        filereader = csv.reader(csvfile)
        #loop through the csv, one row at a time
        for line in filereader:
            Item(line[0], int(line[1]))

def print_price(p):
    print(p)
    item_price.set(f"${p}")


#import tkinter
from tkinter import *
from functools import partial

#LIST TO STORE ITEMS    
all_items = []

generate_items()

# Create GUI
root = Tk()
root.title("Dynamic buttons")
root.resizable(width=FALSE, height=FALSE)
root.geometry("600x400")
item_price= IntVar()
value_lbl = Label(root, textvariable=item_price)
value_lbl.grid(row=2)

# Create button for each item
col = 0
for i in all_items:
    btn = Button(root, text=i.get_item(), command=partial(print_price, i.get_price()))
    btn.grid(row=0, column=col)
    col += 1



root.mainloop()
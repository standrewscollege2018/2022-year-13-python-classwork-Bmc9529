''' This program is used for demonstrating tkinter'''

#import tkinter
from tkinter import *

def say_hello():
    #change the message variable to hello
    if message.get() == "Hello there!":
        message.set("")
    else:
        message.set("Hello there!")

    

def print_input():
    message.set(input_field.get())


#set up root window
root = Tk()
root.title("My first GUI")
root.resizable(width=True, height=False)
root.geometry("800x500")
root.configure(bg="pink")

#set up a label that displays hello from the button
#set up a stringVar to store the text for the label
message = StringVar()
message_lbl = Label(root, textvariable=message, bg="pink")
message_lbl.grid(row=2, column=1)

#Add a label
heading_lbl = Label(root, text="A great Gui", fg="black", bg="pink", font=("Comic Sans MS", 25))
heading_lbl.grid(row=0, column=0)

#add a button
pushme_btn = Button(root, text="Push Me!", width=30, height=3, command=say_hello)
pushme_btn.grid(row=1, column=1)

#get user input from entry field
get_btn = Button(root, text="Get input", width=30, height=5, command=print_input)
get_btn.grid(row=4, column=1)

input_field = Entry(root)
input_field.grid(row=5, column=1)

#start the program by running gui
root.mainloop()


    

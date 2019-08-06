# Some sources I'm using as tutorials:
# https://pythonprogramming.net/tkinter-menu-bar-tutorial/?completed=/tkinter-tutorial-python-3-event-handling/
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html

import tkinter
from tkinter import Tk, Label, Button, S, W, Menu, Frame

# We create class "Window" and inheriting from the "Frame" class,
# which is already in the tkinter module.
class Window(Frame):
    # Next, we define settings upon initialization. We specify parameters
    # that we want to send through the Frame class. We also reference
    # the master widget, which is the tk window.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # And now we run "init_window", which is defined below.
        self.init_window()
    
    def init_window(self):
        # Creating a menu instance
        menu = Menu(self.master) 
        self.master.config(menu=menu)
        # CREATING A MENU AND ITS ITEMS IS A THREE-STEP PROCESS
        file = Menu(menu) # 1. We create the menu 'file'
        file.add_command(label="Exit", command=self.client_exit) # 2. We add the command,
        # give it a name, and specify which command runs when it is clcked
        menu.add_cascade(label="File", menu=file) # 3. We add the menu 'file' to the menu toolbar
    
    def client_exit(self):
        exit()

main_window = Tk()
main_window.title("This is a title.")
main_window.geometry("700x400")

author_label = Label(main_window, text="Designed by an amateur.", font=("Noto", 10), bg="black", fg="white")
author_label.grid(column=0, row=5, sticky=S+W)

test_gui = Window(main_window)

main_window.mainloop()
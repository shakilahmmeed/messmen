from tkinter import *
from tkinter import messagebox, simpledialog
import sqlite3
from controllers import Member

# Database Connection
conn = sqlite3.connect('db.sqlite3')

if conn:
    # Root Window
    root = Tk()
    root.title('Mess Manager')
    root.geometry('800x500')

    member = Member()

    menu = Menu(root)
    menu.add_command(label='Add Member', command=member.add_member)
    menu.add_command(label='Help')
    root.config(menu=menu)

    button = Button(root, text='Show Name', command=member.show)
    button.grid(row=0, column=0)
else:
    root = Tk()
    root.title('Something Wen Wrong')
    root.geometry('800x500')

root.mainloop()

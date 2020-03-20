from tkinter import simpledialog, messagebox


class Member:
    name = ''

    def __init__(self):
        pass

    def add_member(self):
        self.name = simpledialog.askstring('Member Name', 'Enter the name of the member')

    def show(self):
        messagebox.showinfo('Member Name', 'The member name is ' + self.name)
        print('ok')

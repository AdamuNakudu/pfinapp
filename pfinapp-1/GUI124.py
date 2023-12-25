import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import time

class parentclass(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title('P-Finance App')
        self.geometry('400x300')
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = tk.Frame(self, height=400, width=300)
        container.pack(side='top', fill='none', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #creating a dictionary of the frames
        self.frames = {}
        #adding the components to the dictionary
        for F in (MainPage, SidePage):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(SidePage)   
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
 
#the login page        
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Main Page')
        label.pack(padx=10, pady=10)
        self.create_widgets(controller)
        
    def create_widgets(self, controller):
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()
        
        login_button = tk.Button(
            self, 
            text = 'Login', 
            command=lambda: self.validate_login(controller)
        )
        login_button.pack(side='top', fill=tk.X)
        

        
    def validate_login(self, controller):
        userid = self.username_entry.get()
        password = self.password_entry.get()
        
        if userid == 'admin' and password == 'password':
            messagebox.showinfo('Login successful', 'Login Successful')
            controller.show_frame(SidePage),
            
        else:
            messagebox.showerror("Login failed", 'Wrong Username or Password')

#the app itself        
class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=900, height=900)
        
        label = tk.Label(self, text='Income')
        label.grid(row=5, column=5, pady=0)
        
        self.create_widgets(controller)
        
        switch_window_button = tk.Button(
            self,
            text='Logout',
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.grid(row=3, column=0, columnspan=3, pady=10)
        
    def create_widgets(self, controller):
        
        #monthly income
        text1 = tk.Label(self, text="Monthly Income")
        text1.grid(row=0, column=0, pady=5)
        
        self.text1 = Text(self, width=15, height=1)
        self.text1.insert(END, "" +'\n')
        self.text1.grid(row=0, column=1, pady=5)
        
        self.label1=Label(self, text="", font=('Calibri 15'))
        self.label1.grid(row=4, column=4)
        
        
        submit_income_button = tk.Button(
            self,
            text='Submit Income',
            command= self.print_Income
        )
        submit_income_button.grid(row=0, column=2, pady=5, padx=10)
        
    
        
        
        #expenses
        self.new_expenses_label = tk.Label(self, text="Add New Expense")
        self.new_expenses_label.grid(row=1, column=0, pady=5)
        self.new_expenses = tk.Entry(self)
        self.new_expenses.grid(row=1, column=1, pady=5)
        
        submit_expense_button = tk.Button(
            self,
            text='Submit Expense',
            command=lambda: controller.show_frame(MainPage),
        )
        submit_expense_button.grid(row=1, column=2, pady=5, padx=10)
        

    def print_Income(self):
        
        self.label1.config(text="£"+self.text1.get(1.0, "end-1c"))
        
        
        
        
if __name__ == "__main__":
    testObj = parentclass()
    testObj.mainloop()
            
    
    





    
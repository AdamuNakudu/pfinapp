import customtkinter as ck
import tkinter as tk
from tkinter import messagebox
from tkinter import *

ck.set_appearance_mode('dark')
ck.set_default_color_theme('dark-blue')

class parentclass(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title('P-Finance App')
        self.geometry('385x667')
        self.resizable(width=False, height=False)
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = tk.Frame(self, height=667, width=375)
        container.pack(side='top', fill='both', expand=True)
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
        label.pack(side='top', fill='none', expand=True)
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
        login_button.pack(side='top', fill=tk.X, expand=False)
        
        
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
        tk.Frame.__init__(self, parent, width=375, height=667)
        
        label = tk.Label(self, text='Income', justify=tk.LEFT )
        label.grid(row=5, column=1, pady=0)
        
        self.create_widgets(controller)
        
        switch_window_button = ck.CTkButton(
            self,
            fg_color=('Black', 'black'),
            text='Logout',
            corner_radius=25,
            width=30,
            height=30,
            command=lambda: controller.show_frame(MainPage),
        )
        switch_window_button.grid(row=12, column=0, columnspan=3, pady=10)
        
        #self.config(background=ui.Color.MAIN)
        #the baby blue frame in the middle
        self.cardframe = ck.CTkFrame(self, fg_color='light blue', corner_radius=25 ,height=300, width=340)
        self.cardframe.grid(row=10, column=0, columnspan=3, padx=4 )
    
        
    def create_widgets(self, controller):
        
        #monthly income
        text1 = tk.Label(self, text="Monthly Income")
        text1.grid(row=0, column=0, pady=5)
        
        self.text1 = Text(self, width=15, height=1)
        self.text1.insert(END, "" +'\n')
        self.text1.grid(row=0, column=1, pady=5)
        
        self.label1=Label(self, text="", font=('Calibri 15'))
        self.label1.grid(row=6, column=2)
        
        #ck.set_appearance_mode("Dark")
        
        submit_income_button = ck.CTkButton(
            self,
            fg_color=('Black', 'gray'),
            text='Submit Income',
            command= self.print_Income
        )
        submit_income_button.grid(row=0, column=2, pady=5, padx=10)
        
    
        
        
        #expenses
        self.new_expenses_label = tk.Label(self, text="Add New Expense")
        self.new_expenses_label.grid(row=1, column=0, pady=5)
        self.new_expenses = Text(self, width=15, height=1)
        self.new_expenses.grid(row=1, column=1, pady=5)
        
        submit_expense_button = ck.CTkButton(
            self,
            fg_color=('Black', 'gray'),
            text='Submit Expense',
            command=self.print_Income
        )
        submit_expense_button.grid(row=1, column=2, pady=5, padx=10)
        

    def print_Income(self):
        income_text = self.text1.get(1.0, "end-1c").strip()
        if income_text:  # Check if there is any text in the entry
            current_label_text = self.label1.cget("text")
            if current_label_text:
                new_label_text = current_label_text + "\n" + "£" + income_text
            else:
                new_label_text = "£" + income_text
            self.label1.config(text=new_label_text)
        else:
        # Handle the case where there is no text in the entry
            print("Please enter a valid income.")
            
            #self.label1.config(text="£"+self.text1.get(1.0, "end-1c"))
        
        
if __name__ == "__main__":
    testObj = parentclass()
    testObj.mainloop()
            
    
    





    
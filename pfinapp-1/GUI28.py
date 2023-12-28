import customtkinter as ck
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as tkk

ck.set_appearance_mode('dark')
ck.set_default_color_theme('dark-blue')

class parentclass(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title('P-Finance App')
        self.geometry('385x667')
        self.resizable(width=False, height=False)
        self.configure(background='white')
        self.userid = None
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = ck.CTkFrame(self, height=667, width=375)
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
            controller.userid = userid
            controller.show_frame(SidePage),
        
            
        else:
            messagebox.showerror("Login failed", 'Wrong Username or Password')
        
    
    
    

#the app itself        
class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=375, height=667)
        self.grid_rowconfigure(10, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.configure(background='gray25')
        

        userid = controller.userid

        self.TitlelabelFrame = ck.CTkFrame(self, fg_color='gray50', height=20, width=320)
        self.TitlelabelFrame.grid(row=0, column=0, columnspan=3, pady=0, padx= 0)
        
        self.Titlelabel = tk.Label(self.TitlelabelFrame, text=f'Hi {userid} 👋', justify=tk.LEFT, font=('Helvetica bold', 26))
        self.Titlelabel.configure(background='gray25')
        self.Titlelabel.grid(row=0, column=1, pady=0)
        
        
        
        #self.config(background=ui.Color.MAIN)
        #-  -   -the top grey box detailing total balance of the month- -   -   
        self.cardframe = ck.CTkFrame(self, fg_color='gray50', corner_radius=25 ,height=120, width=340)
        self.cardframe.grid(row=1, column=0, columnspan=20, padx=4, pady=5)
        
        self.cardframe.propagate(False) #this stops any labels from fitting to the fram itself, negating it
        
        #-   -  -   -   - The middle grey box -  -   -   -   -   -
        self.Middleframe = ck.CTkFrame(self, fg_color='gray50', corner_radius=25 ,height=440, width=340)
        self.Middleframe.grid(row=2, column=0, columnspan=20, padx=4, pady=5)
        
        self.Middleframe.propagate(False) #this stops any labels from fitting to the fram itself, negating it
        
        
        
        #-  -   -   -   -The balance title!!-   -   -   -   -   -   
        self.cardframelabel = tk.Label(
            self.cardframe,
            text='Balance:',
            font=('Helvetica', 16, 'bold'),
            fg='white',
            bg='gray50',
            borderwidth=0,
            highlightthickness=0,
            state='normal',
            relief=FLAT,
            #relief=SOLID,
            
        )
        #self.cardframelabel.grid(row=1, column=0, padx=10, pady=10)
        self.cardframelabel.pack(side=tk.TOP, anchor=NW, padx=10, pady=10)
        
        #-  -   -   -   -The balance no.!-  -   -   -   -   -   -   
        self.BalanceFrame = ck.CTkFrame(
            self.cardframe, width=100, height=60, fg_color='gray50' 
        )
        self.BalanceFrame.pack(side=tk.TOP, anchor=NE, padx=10, pady=0 )
        self.BalanceFrame.place(x=160, y=7)
        #self.BalanceFrame.propagate(False)
        
        self.Balance= tk.Label(
            self.BalanceFrame,
            text='£100,000',
            font=('Helvetica', 36, 'bold'),
            fg='blue4',
            bg='gray50',
            borderwidth=0,
            highlightthickness=0,
            state='normal',
            relief=FLAT,
        )
        self.Balance.pack(side=tk.TOP, anchor=NE, padx=10, pady=0)
        
        
        #-  -   -   -   -spent and income labels!!  -   -   -   -   -
        
        self.IncomeLabel = tk.Label(
            self.cardframe,
            text='INCOME: '+ 'Null',
            bg='gray50',
            justify='left',
            highlightthickness=0,
        )
        self.IncomeLabel.pack(
            side=tk.TOP, fill=tk.X, expand=True, anchor='w', padx=0
        )
        self.IncomeLabel.place(x=100, y=65)
        
        self.ExpensesLabel = tk.Label(
            self.cardframe,
            text='EXPENSES: '+' +£2300',
            bg='gray50',
            justify='left',
            borderwidth=0,
            highlightthickness=0,
        )
        self.ExpensesLabel.pack(
            side=tk.TOP, fill=tk.X, expand=True, anchor='w', padx=0
        )
        self.ExpensesLabel.place(x=100, y=85)
        
        #-  -   -  -   -Creating analytics sections-   -   -   -   -   -
        self.EntryForm = ck.CTkFrame(self, fg_color='dark blue',width=380, corner_radius=25)
        self.EntryForm.grid_columnconfigure((0,3), minsize=40)
        #self.EntryForm.grid(row=0, column= 0)
    
        self.create_widgets(controller)
        
    
        
    def create_widgets(self, controller):
        
        #monthly income
        text1 = tk.Label(self, text="Monthly Income")
        text1.grid(row=2, column=0, pady=5)
        
        self.text1 = Text(self, width=15, height=1)
        self.text1.insert(END, "" +'\n')
        self.text1.grid(row=2, column=1, pady=5)
        
        self.label1=Label(self, text="", font=('Calibri 15'))
        self.label1.grid(row=2, column=2)
        
        #ck.set_appearance_mode("Dark")
        
        submit_income_button = ck.CTkButton(
            self,
            fg_color=('Black', 'gray'),
            text='Submit Income',
            command= self.print_Income
        )
        submit_income_button.grid(row=2, column=2, pady=5, padx=10)
        
        
        #expenses
        self.new_expenses_label = tk.Label(self, text="Add New Expense")
        self.new_expenses_label.grid(row=3, column=0, pady=5)
        self.new_expenses = Text(self, width=15, height=1)
        self.new_expenses.grid(row=3, column=1, pady=5)
        
        submit_expense_button = ck.CTkButton(
            self,
            fg_color=('Black', 'gray'),
            text='Submit Expense',
            command=self.print_Income
        )
        submit_expense_button.grid(row=3, column=2, pady=5, padx=10)
        
        
        switch_window_button = ck.CTkButton(
            self,
            fg_color=('Black', 'dark blue'),
            text='+',
            corner_radius=50,
            width=30,
            height=30,
            command=lambda:self.ToggleAnimation(controller),
        )
        switch_window_button.grid(row=3, column=0, columnspan=3, pady=10, sticky ='s')
        
        #log out command: command=lambda: controller.show_frame(MainPage),
        
        
        
    def PlusAnimation(self, controller):
        for y in range(-60, -13, 1):
            self.EntryForm.update()
            self.EntryForm.place(relx=0.5, rely=0.5, y=y**2 - 20, anchor='center')
            
    def HideAnimation(self):
        for y in range(13, 60, 1):
            self.EntryForm.update()
            self.EntryForm.place(relx=0.5, rely=0.5, y=y**2, anchor='center')
        self.EntryForm.place_forget()    
        
    def ToggleAnimation(self, controller):
        if self.EntryForm.winfo_ismapped():
            self.HideAnimation()
        else:
            self.PlusAnimation(controller)
    
    def print_Income(self):
        income_text = self.text1.get(1.0, "end-1c").strip()
        if income_text:  # Check if there is any text in the entry
            new_label_text = 'INCOME:   £' + income_text
            self.IncomeLabel.config(text=new_label_text)
        else:
        # Handle the case where there is no text in the entry
            print("Please enter a valid income.")
            #self.IncomeLabel.config(text="£"+self.text1.get(1.0, "end-1c"))
        
        
if __name__ == "__main__":
    testObj = parentclass()
    testObj.mainloop()
            
    
    





    
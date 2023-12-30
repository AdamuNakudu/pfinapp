import customtkinter as ck
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.ttk as tkk
from PIL import ImageTk, Image
from tkinter import Frame

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
            
        self.show_frame(MainPage)   
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
 
#the login page        
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#574237')
        
        LoginFrame = Canvas(self, width=385, height=400, background='#574237', highlightthickness=0)
        LoginFrame.pack(side='top', fill='none', expand=False)
        LoginFrame.place(anchor='center', relx=0.5, rely=0.5)
        
        
        self.mainpageimg = ImageTk.PhotoImage(Image.open("cashicon.png").convert(mode='RGBA').resize((92,100)))
        
        
        LoginFrame.create_image(193,100, anchor=CENTER, image=self.mainpageimg)
        
        #label = tk.Label(LoginFrame,image=mainpageimg, text='Main Page')
        #label.pack(padx=10, pady=10)
        #label.pack(side='top', fill='none', expand=True)
        
        self.create_widgets(controller)
        
        
    def create_widgets(self, controller):
        
        # ----- Clicking on and away from username to indicate where to type -----
        def on_clickusername(event):
            if self.username_entry.get() == 'Username':
                self.username_entry.delete(0, END)
                self.username_entry.insert(0, '')
                self.username_entry.config(fg='white')
        def on_clickawayusername(event):
            if self.username_entry.get() == '':
                self.username_entry.insert(END, 'Username')
                self.username_entry.config(foreground='gray30')
            
                
        # - -   -   -   -   -   -USERNAME ENTRY-    -   -   -   -   -       
                
        self.username_entry = tk.Entry(self, fg='gray30', justify='center')
        self.username_entry.insert(END, 'Username') #default text inside input
        self.username_entry.pack()
        self.username_entry.place(x=0, y=40, anchor='center', relx=0.5, rely=0.5)
        
        self.username_entry.bind('<FocusIn>', on_clickusername)
        self.username_entry.bind('<FocusOut>', on_clickawayusername)
        
        
        #-  -   -   -   -   -   -PASSWORD ENTRY-    -   -   -   -   -   
    
        def on_clickpassword(event):
            if self.password_entry.get() == 'Password':
                self.password_entry.delete(0, END)
                self.password_entry.insert(0, '')
                self.password_entry.config(show='*',fg='white')
        def on_clickawaypassword(event):
            if self.password_entry.get() == '':
                self.password_entry.insert(END, 'Password')
                self.password_entry.config(show='', foreground='gray30')
            
            
        self.password_entry = tk.Entry(self, fg='gray30', justify='center')
        self.password_entry.insert(END, 'Password') #default text inside input
        self.password_entry.pack()
        self.password_entry.place(x=0, y=70, anchor='center', relx=0.5, rely=0.5)
        
        self.password_entry.bind('<FocusIn>', on_clickpassword)
        self.password_entry.bind('<FocusOut>', on_clickawaypassword)
        
        login_button = tk.Button(
            self, 
            text = 'Login', 
            background='#574237',
            highlightcolor='#574237',
            highlightbackground='#574237',
            command=lambda: self.validate_login(controller)
        )
        login_button.pack(side='top', fill=tk.X, expand=False)
        login_button.place(x=0, y=100, anchor='center', relx=0.5, rely=0.5)
        #login_button.place(anchor='center', relx=0.5, rely=0.5)
        

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
        self.configure(background='#574237')
        
        self.total_expenses = 0

        userid = controller.userid
        

        self.TitlelabelFrame = tk.Frame(self, bg='gray50', height=20, width=320)
        self.TitlelabelFrame.grid(row=0, column=0, columnspan=3, pady=0, padx= 0)
        
        self.Titlelabel = tk.Label(self.TitlelabelFrame, text=f'Hi {userid} 👋', justify=tk.CENTER, font=('Helvetica bold', 26))
        self.Titlelabel.configure(background='gray25', borderwidth=150)
        self.Titlelabel.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
        
        
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
            text='£0.00',
            font=('Helvetica', 36, 'bold'),
            fg='tomato3',
            bg='gray50',
            borderwidth=0,
            highlightthickness=0,
            state='normal',
            relief=FLAT,
            wraplength=150
        )
        self.Balance.pack(side=tk.TOP, anchor=NE, expand=False, fill=None, padx=10, pady=0)
        
        
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
        
        self.ExpenseBreakdownLabel = tk.Label(
            self.Middleframe,
            text='EXPENSE BREAKDOWN',
            bg='gray50',
            justify='center',
            highlightthickness=0,
            borderwidth=0,
        )
        self.ExpenseBreakdownLabel.pack(
            side=tk.TOP, fill=tk.X, expand=False, anchor=N, padx=10, pady=5
        )
        
        #-  -   -   -   -Middle frame listing expenses- -   -   -   -   
        self.NewExpensesListLabel = tk.Label(
            self.Middleframe,
            text='EXPENSES',
            bg='gray50',
            justify='right',
            highlightthickness=0,
        )
        self.NewExpensesListLabel.pack(
            side=tk.TOP, fill=tk.NONE, expand=False, anchor=E, padx=10
        )
        
        self.TotalExpense= tk.Label(
            self.Middleframe,
            text='Total Expenses',
            bg='gray50',
            justify='left',
            highlightthickness=0,
        )
        self.TotalExpense.pack(
            side=tk.BOTTOM, fill=tk.NONE, expand=False, anchor=SW, padx=10, pady=10,
        )
        
        self.TotalExpenseNum= tk.Label(
            self.Middleframe,
            text='£0',
            bg='gray50',
            justify='right',
            highlightthickness=0,
        )
        self.TotalExpenseNum.pack(
            side=tk.BOTTOM, fill=tk.NONE, expand=False, anchor=SE, padx=10, pady=10
        )
        self.TotalExpenseNum.place(x=250, y=408)
        
        
        #-  -   -  -   -Creating analytics sections-   -   -   -   -   -
        self.EntryForm = ck.CTkFrame(self, fg_color='gray70',width=380, corner_radius=25)
        self.EntryForm.grid_columnconfigure((0,3), minsize=40)
        self.EntryForm.propagate(False)
        #self.EntryForm.grid(row=0, column= 0)
    
        self.create_widgets(controller)
        
    
        
    def create_widgets(self, controller):
        
        #monthly income
        text1 = tk.Label(self.EntryForm, text="Monthly Income")
        #text1.grid(row=2, column=0, pady=5)
        text1.pack(side=tk.TOP, fill=tk.X)
        
        self.text1 = Text(self.EntryForm, width=15, height=1)
        self.text1.insert(END, "" +'\n')
        #self.text1.grid(row=2, column=1, pady=5)
        self.text1.pack(side=tk.TOP, fill=tk.X)
        
        #self.label1=Label(self, text="", font=('Calibri 15'))
        #self.label1.grid(row=2, column=2)
        
        #ck.set_appearance_mode("Dark")
        
        submit_income_button = ck.CTkButton(
            self.EntryForm,
            fg_color=('black', 'gray'),
            text='Submit Income',
            command= lambda:[self.print_Income(controller), 
            self.print_Income_Balance(controller),
            self.print_Balance(controller)]
        )
        #submit_income_button.grid(row=2, column=2, pady=5, padx=10)
        submit_income_button.pack(side=tk.TOP, fill=tk.X)
        
        
        #expenses
        self.new_expenses_label = tk.Label(self.EntryForm, text="Add New Expense")
        self.new_expenses_label.propagate(False)
        #self.new_expenses_label.grid(row=3, column=0, pady=5)
        self.new_expenses_label.pack(side=tk.TOP, fill=tk.X)
        
        self.new_expenses = Text(self.EntryForm, width=15, height=1)
        self.new_expenses.insert(END, "" +'\n')
        self.new_expenses.pack(side=tk.TOP, fill=tk.X)
        
        submit_expense_button = ck.CTkButton(
            self.EntryForm,
            fg_color=('Black', 'gray'),
            text='Submit Expense',
            command=lambda:[self.print_Expenses(controller),
            self.print_Income_Balance(controller),
            self.print_Balance(controller)]
        )
        #submit_expense_button.grid(row=3, column=2, pady=5, padx=10)
        submit_expense_button.pack(side=tk.TOP, fill=tk.X)
        
        
        switch_window_button = ck.CTkButton(
            self,
            fg_color=('Black', 'dark blue'),
            text='+',
            corner_radius=50,
            width=30,
            height=30,
            command=lambda:self.ToggleAnimation(controller),
        )
        switch_window_button.grid(row=3, column=4, pady=10, sticky ='s')
        switch_window_button.place(x=170, y=625)
        
        submit_logout_button = ck.CTkButton(
            self.EntryForm,
            fg_color=('black', 'gray'),
            text='Logout',
            width=5,
            height=5,
            command=lambda: controller.show_frame(MainPage),
        )
        #submit_income_button.grid(row=2, column=2, pady=5, padx=10)
        submit_logout_button.pack(side=tk.BOTTOM, fill=tk.NONE)
        
        
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
    
    def print_Income(self, controller):
        income_text = self.text1.get(1.0, "end-1c").strip()
        if income_text:  # Check if there is any text in the entry
            new_label_text = 'INCOME:   £' + income_text
            self.IncomeLabel.config(text=new_label_text)
        else:
        # Handle the case where there is no text in the entry
            print("Please enter a valid income.")
            #self.IncomeLabel.config(text="£"+self.text1.get(1.0, "end-1c"))
            
    def print_Income_Balance(self, controller):
        income_text = self.text1.get(1.0, "end-1c").strip()
        if income_text:  # Check if there is any text in the entry
            new_label_text = '£' + income_text
            self.Balance.config(text=new_label_text)
        else:
        # Handle the case where there is no text in the entry
            print("Please enter income.")
        
    def print_Expenses(self, controller):
        Expenses_text = self.new_expenses.get(1.0, "end-1c").strip()
        if Expenses_text:  # Check if there is any text in the entry
            current_label_text = self.NewExpensesListLabel.cget("text")
            if current_label_text:
                new_label_text = current_label_text + "\n" + "£" + Expenses_text
            else:
                new_label_text = "£" + Expenses_text
            self.NewExpensesListLabel.config(text=new_label_text)
            
            #calculates total expenses
            expenses_lines = new_label_text.split('\n')
            expenses_values = [float(expense.strip('£')) for expense in expenses_lines if '£' in expense]
            

            self.total_expenses = sum(expenses_values)
            #total_expenses = sum(float(expense.strip('£')) for expense in new_label_text.split('\n'))
            self.TotalExpenseNum.config(text=f' £{self.total_expenses}')
            
            
        else:
        # Handle the case where there is no text in the entry
            print("Please enter an Expense.")
            
    def print_Balance(self, controller):
        
        income_text = self.text1.get(1.0, "end-1c").strip()
        #Expenses_text = self.new_expenses.get(1.0, "end-1c").strip()
        #Expenses_text = float(Expenses_text.strip('£'))
        Expenses_text= float(self.total_expenses)
        
        if income_text:
            income_text = self.text1.get(1.0, "end-1c").strip()
            income_text = float(income_text.strip('£'))
        
        if income_text and Expenses_text:
            new_label_text = '£' + str(income_text - Expenses_text)
            self.Balance.config(text=new_label_text)
        else:
            print('Both income AND expense have to be entered to calculate balance')
            
    def clear_Expenses(self, controller):
        self.NewExpensesListLabel.config(text='0')
        
if __name__ == "__main__":
    testObj = parentclass()
    testObj.mainloop()
            
    
    





    
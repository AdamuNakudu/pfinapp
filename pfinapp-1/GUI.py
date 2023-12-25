import tkinter as tk
from tkinter import messagebox 

class mainapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        
        self.title('P-Finance Desktop App')
        self.geometry('400x300')
        self._frame = None
        
        self.frames = {}
        for F in (login, MainFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            #frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(login)
        
    def show_frame(self, page_name):
        frame = self.frames[login]
        frame.tkraise()            
            
class login(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.create_widgets()
    
        
    def create_widgets(self):
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()
        
        login_button = tk.Button(self, text = 'Login', command=self.validate_login)
        login_button.pack()
    
    def validate_login(self):
        
        userid = self.username_entry.get()
        password = self.password_entry.get()
        
        if userid == 'admin' and password == 'password':
            messagebox.showinfo('Login successful')
            self.switch_frame(MainFrame)
        else:
            messagebox.showerror('Login failed')
            
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame()

class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.create_widgets()
        app = tk.Tk()
        app.title('P-Finance Desktop App')
        app.geometry('400x300')
        self.pack()
        self.mainloop()
        
    #def create_widgets(self):
        
        
    def on_submit():
        pass


    def main():
        label = tk.Label(self, text='Monthly Income')
        label.pack()

        entry = tk.Entry(self)
        entry.pack()

        submit_button = tk.Button(self, text='Submit', command= on_submit)
        submit_button.pack()

if __name__ == '__main__':
    app = mainapp()
    app.mainloop()
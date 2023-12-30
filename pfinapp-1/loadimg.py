from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("1400x1000")

img = Image.open("cashicon.png").convert(mode="RGBA")


resized = img.resize((500, 600))

img = ImageTk.PhotoImage(resized)




bg1 = Image.open("blackbg.png")

resizedbg = bg1.resize((500,600))

bg1 = ImageTk.PhotoImage(resizedbg)

frame = Canvas(win, width=500, height=600, bg='blue')
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


# Create an object of tkinter ImageTk


# Create a Label Widget to display the text or Image
#frame.create_image(0,1, anchor=NW, image= bg1)
frame.create_image(0,0, anchor=NW, image=img)

#label = Label(frame, image = img)
#label.pack()

win.mainloop()
from tkinter import *
from PIL import ImageTk, Image
wn = Tk()

# canvas = Canvas(wn, width=300, height=300)
# image = ImageTk.PhotoImage(Image.open('myIcon..png'))
# canvas.create_image(0,0, anchor-NW, image-image)
# canvas.pack()

img = ImageTk.PhotoImage(Image.open('myIcon..png'))
wn.geometry('400x400')
label = Label(wn, image=img)
label.pack()

wn.iconbitmap('')
myMenu = Menu(wn)
wn.config(menu=myMenu)
#e
file_menu = Menu(myMenu)
myMenu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
# file_menu.add_separator()
file_menu.add_command(label='option')
file_menu.add_command(label='option')
file_menu.add_command(label='option')
file_menu.add_command(label='option')
wn.mainloop()

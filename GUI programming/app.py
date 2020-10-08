from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import turtle

def app(screen):
    # set up the screen
    screen = screen
    width = screen.winfo_screenwidth()
    height = screen.winfo_screenheight()
    screen.title('app')
    screen.iconbitmap('myico.ico')
    screen.geometry('%dx%d+0+0' % (width, height))
    screen.configure(bg='#FFA900')
    
    # Freames
    left_frame = Frame(screen, bg='#00ff00')
    left_frame.pack(side='left')
    Label(left_frame, text='left').pack()
    right_frame = Frame(screen, bg='#110ff9')
    right_frame.pack(side='right')
    Label(right_frame, text='right').pack()
    screen.mainloop()



# app(Tk())

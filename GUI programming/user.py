from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3
from Creating_new_account import create_new_account
from forget_password import forgetPassword
from app import app

screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
screen.title('Login')
screen.iconbitmap('myico.ico')
screen.geometry('%dx%d+0+0' % (width, height))
screen.configure(bg='#FFA900')

data = []
# ======================= cerating a database ================================================
'''
conn = sqlite3.connect('registration.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS registration(
            first_name text,
            last_name text,
            username text,
            password text
            )""")

conn.commit()

conn.close()
'''


# =============================================================================================

# Creating a new account function
def new_account():
    screen2 = Toplevel()
    create_new_account(screen2)


def forget():
    screen = Toplevel()
    forgetPassword(screen)


# the starting page of the app
def start():
    # Space between frames
    space_label = Label(screen, text=' ', font=('Comic Sans MS', 10, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()

    
    # login frame and label
    login_frame = Frame(screen, bg='#009fff', bd=5)
    
    login_frame.pack()
    
    space_label = Label(login_frame, text=' ', font=('Comic Sans MS', 3, 'bold'))
    space_label.configure(bg='#009fff')
    space_label.pack()
    
    # logo  Frame with its labels
    Logo_frame = Frame(login_frame)
    Logo_frame.configure(bg='#009fff')
    Logo_frame.pack()

    logo_img = ImageTk.PhotoImage(Image.open('myico.ico'))
    Logo_label = Label(Logo_frame, image=logo_img)
    Logo_label.configure(bg='#009fff')
    Logo_label.pack()
    

    user_label = Label(login_frame, text='Log in', font=('Comic Sans MS', 40, 'bold'))
    user_label.configure(bg='#009fff')
    user_label.pack()

    space_label = Label(login_frame, text='', font=('Comic Sans MS', 20, 'bold'))
    space_label.configure(bg='#009fff')
    space_label.pack()

    # Email Frame label and widget
    Email_frame = Frame(login_frame)
    Email_frame.configure(bg='#009fff')
    Email_frame.pack()
    
    Email_label = Label(Email_frame, text='  Username\t  ', font=('Comic Sans MS', 10, 'bold'))
    Email_label.configure(bg='#009fff')
    Email_label.pack(side='left')

    Email_entrty = Entry(Email_frame, width=30, font=('Comic Sans MS', 10))
    Email_entrty.pack(side='right')

    space_label = Label(login_frame, text='', font=('Comic Sans MS', 6, 'bold'))
    space_label.configure(bg='#009fff')
    space_label.pack()

    # password labels and widgets
    password_frame = Frame(login_frame)
    password_frame.configure(bg='#009fff')
    password_frame.pack()

    password_label = Label(password_frame, text='  Password\t  ', font=('Comic Sans MS', 10, 'bold'))
    password_label.configure(bg='#009fff')
    password_label.pack(side='left')

    password_entrty = Entry(password_frame, width=30, show='*', font=('Comic Sans MS', 10, 'bold'))
    password_entrty.pack(side='right')

    # space
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 4, 'bold'))
    space_label.configure(bg='#009fff')
    space_label.pack()

    # create a button of forgetting password
    forgetButton = Button(login_frame, text='forget password', command=forget, bd=0, fg='#f90000',
                          font=('Time New Roman', 11, 'underline'))
    forgetButton.configure(bg='#009fff')
    forgetButton.pack()

    # space
    space_label = Label(login_frame, text=' ', font=('Comic Sans MS', 15, 'bold'))
    space_label.configure(bg='#009fff')
    space_label.pack()

    # create a login function
    def login():
        Email = str(Email_entrty.get())
        password = str(password_entrty.get())
        # checking user data
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("SELECT *FROM registration WHERE username=?", (Email, ))
        data = c.fetchone()

        conn.commit()

        conn.close()

        if Email == '' or password == '':
            tkinter.messagebox.showerror('Error', 'You must fill all the blanks')

        elif data is None:
            tkinter.messagebox.showerror('Error', 'Invalid username, Please check your username')
        
        elif password not in data:
            tkinter.messagebox.showerror('Error', 'Incorrect password, Please check your password')
            
        elif (Email != '' and password != '') and \
                (Email in data and password in data):
            Email_entrty.delete(0, END)
            password_entrty.delete(0, END)
            screen.deletecommand(str(Logo_frame))
            screen.deletecommand(str(login_frame))
            screen.deletecommand(str(Account_frame))
            app(screen)

    # Button of log in
    Login = Button(login_frame, text='Login', command=login, width=10, padx=50, pady=5,
                   font=('Time new roman', 12, 'bold'))
    Login.configure(bg='#00f100', fg='#ffffff')
    Login.pack()

    # space between frames
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 5, 'bold'))
    space_label.configure(bg='#009fff')
    space_label.pack()

    # space between frames
    space_label = Label(screen, text='', font=('Comic Sans MS', 15, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # Create a new account with its frame and button
    Account_frame = Frame(screen)
    Account_frame.configure(bg='#FFA900')
    Account_frame.pack()

    Account_button = Button(Account_frame, text='Create a new account', command=new_account,
                            width=23, font=('Bauhaus 93', 20, 'bold'))
    Account_button.configure(bg='#f90000')
    Account_button.pack()

    screen.mainloop()


start()

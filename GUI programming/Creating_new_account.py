from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3


def create_new_account(screen):
    screen = screen
    screen.title('Creating a news account')
    screen.iconbitmap('myico.ico')
    screen.geometry('500x650')
    screen.configure(bg='#FFA900')
    screen.resizable(False, False)
    
    # logo  Frame with its labels
    Logo_frame = Frame(screen)
    Logo_frame.configure(bg='#FFA900')
    Logo_frame.pack()
    
    logo_img = ImageTk.PhotoImage(Image.open('myico.ico'))
    Logo_label = Label(Logo_frame, image=logo_img)
    Logo_label.configure(bg='#FFA900')
    Logo_label.pack()
    
    # Space between frames
    space_label = Label(screen, text='', font=('Comic Sans MS', 7, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # login frame and label
    login_frame = Frame(screen, bg='#ccffcc', bd=8)
    login_frame.pack()
    
    user_label = Label(login_frame, text='Create a new account', font=('Comic Sans MS', 20, 'bold'))
    user_label.configure(bg='#ccffcc')
    user_label.pack()
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 10, 'bold'))
    space_label.configure(bg='#ccffcc')
    space_label.pack()
    
    # first name Frame label and widget
    firstName_frame = Frame(login_frame)
    firstName_frame.configure(bg='#ccffcc')
    firstName_frame.pack()
    
    firstName_label = Label(firstName_frame, text='  First Name    \t', font=('Comic Sans MS', 10, 'bold'))
    firstName_label.configure(bg='#ccffcc')
    firstName_label.pack(side='left')
    
    firstName_entrty = Entry(firstName_frame, width=30, font=('Comic Sans MS', 10))
    firstName_entrty.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 6, 'bold'))
    space_label.configure(bg='#ccffcc')
    space_label.pack()
    
    # last name Frame label and widget
    lastName_frame = Frame(login_frame)
    lastName_frame.configure(bg='#ccffcc')
    lastName_frame.pack()
    
    lastName_label = Label(lastName_frame, text='  Last Name    \t', font=('Comic Sans MS', 10, 'bold'))
    lastName_label.configure(bg='#ccffcc')
    lastName_label.pack(side='left')
    
    lastName_entrty = Entry(lastName_frame, width=30, font=('Comic Sans MS', 10))
    lastName_entrty.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 6, 'bold'))
    space_label.configure(bg='#ccffcc')
    space_label.pack()
    
    # username Frame label and widget
    username_frame = Frame(login_frame)
    username_frame.configure(bg='#ccffcc')
    username_frame.pack()
    
    username_label = Label(username_frame, text='  Username    \t', font=('Comic Sans MS', 10, 'bold'))
    username_label.configure(bg='#ccffcc')
    username_label.pack(side='left')
    
    username_entrty = Entry(username_frame, width=30, font=('Comic Sans MS', 10))
    username_entrty.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 6, 'bold'))
    space_label.configure(bg='#ccffcc')
    space_label.pack()
    
    # password Frame label and widget
    password_frame = Frame(login_frame)
    password_frame.configure(bg='#ccffcc')
    password_frame.pack()
    
    password_label = Label(password_frame, text='  Create password   ', font=('Comic Sans MS', 10, 'bold'))
    password_label.configure(bg='#ccffcc')
    password_label.pack(side='left')
    
    password_entrty = Entry(password_frame, width=30, show='*', font=('Comic Sans MS', 10))
    password_entrty.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 6, 'bold'))
    space_label.configure(bg='#ccffcc')
    space_label.pack()
    
    # confirm password Frame label and widget
    Conpassword_frame = Frame(login_frame)
    Conpassword_frame.configure(bg='#ccffcc')
    Conpassword_frame.pack()
    
    Conpassword_label = Label(Conpassword_frame, text='  Confirm password  ', font=('Comic Sans MS', 10, 'bold'))
    Conpassword_label.configure(bg='#ccffcc')
    Conpassword_label.pack(side='left')
    
    Conpassword_entrty = Entry(Conpassword_frame, width=30, show='*', font=('Comic Sans MS', 10))
    Conpassword_entrty.pack(side='right')
    
    space_label = Label(login_frame, text='', font=('Comic Sans MS', 6, 'bold'))
    space_label.configure(bg='#ccffcc')
    space_label.pack()
    
    def saveData():
        first_name = str(firstName_entrty.get())
        last_name = str(lastName_entrty.get())
        username = str(username_entrty.get())
        password = str(password_entrty.get())
        conpassword = str(Conpassword_entrty.get())
        # checking user data
        conn = sqlite3.connect('registration.db')
        c = conn.cursor()
        c.execute("SELECT *FROM registration WHERE username=?", (username,))
        data = c.fetchone()
        conn.commit()
        
        def check():
            for i in range(10):
                if str(i) in first_name or str(i) in last_name:
                    status = True
                    return status
        
        if first_name == '' or last_name == '' or username == '' or password == '' or conpassword == '':
            tkinter.messagebox.showerror('Error', 'You must fill all the blanks')
        
        elif len(first_name) < 3 or len(last_name) < 3:
            tkinter.messagebox.showerror('Error', 'First name or last name must be atleast 3 characters')
        
        elif check():
            tkinter.messagebox.showerror('Error', "First name or last name can't contain numerals")
            
        elif str('@') not in str(username):
            tkinter.messagebox.showerror('Error', 'username must contain @')
        
        elif ' ' in username:
            tkinter.messagebox.showerror('Error', "Username can't contain spaces\n"
                                                  "Use _ or -")
        
        elif data is not None:
            tkinter.messagebox.showwarning('Error', 'This username have already taken')
        
        elif ' ' in password:
            tkinter.messagebox.showerror('Error', "Password can't contain spaces")
            
        elif len(password) < 8:
            tkinter.messagebox.showerror('Error', 'Your password must be atleast 8 characters')
        
        elif len(password) > 14:
            tkinter.messagebox.showerror('Error', "Your password must be less than 14 characters")
            
        elif password != conpassword:
            tkinter.messagebox.showerror("Error", 'Your Confirmation password must be same as create password')
        
        elif password == conpassword:
            firstName_entrty.delete(0, END)
            lastName_entrty.delete(0, END)
            username_entrty.delete(0, END)
            password_entrty.delete(0, END)
            Conpassword_entrty.delete(0, END)
            # saving data in a data base
            conn = sqlite3.connect('registration.db')
            c = conn.cursor()
            c.execute("INSERT INTO registration VALUES(:first_name, :last_name, :username, :password)",
                      (first_name, last_name, username, password))
            conn.commit()
            conn.close()
    
    # Button of log in
    Login = Button(login_frame, text='Submit', command=saveData, width=10, font=('Comic Sans MS', 10, 'bold'))
    Login.configure(bg='#00f100')
    Login.pack()
    
    # space between frames
    space_label = Label(screen, text='', font=('Comic Sans MS', 20, 'bold'))
    space_label.configure(bg='#FFA900')
    space_label.pack()
    
    # Create a new account with its frame and button
    Account_frame = Frame(screen)
    Account_frame.configure(bg='#FFA900')
    Account_frame.pack()
    
    screen.mainloop()


# create_new_account(Tk())

from tkinter import *
from PIL import ImageTk, Image
import sqlite3
wn = Tk()
wn.title('Competition')
wn.configure(bg='brown')
wn.geometry('500x500')


# create a database and connect to your file
conn = sqlite3.connect('login.db')

# creat a curser
c = conn.cursor()

# create a table

# c.execute("""CREAT TABLE login(
#     first_name text,
#     last_name text,
#     country text,
#     phone number text
# )""")
#

# commit changes
conn.commit()

#close connection
conn.close()
wn.mainloop()
'''import random

import sqlite3

name = input('first name: ')
nam = input('last name: ')


def c():
    conn = sqlite3.connect('regn.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS regn(
                first_name text,
                last_name text,
                username text,
                password text
                )""")

    #c.execute("INSERT INTO regn VALUES('Alii', 'Hasan', '@Alii', 223355)")
    c.execute("SELECT  * FROM regn WHERE first_name=? AND last_name=?", (name, nam))

    d = c.fetchone()

    if d is None:
        print('incorrect name')

    else:
        print(d)
        # f = input('Rp1: ')
        l = input('Rp2: ')
        c.execute("UPDATE regn SET last_name = ? WHERE first_name = ?",(l,name, ))
        conn.commit()
        c.execute("SELECT  * FROM regn WHERE first_name='Ali'")
        h = c.fetchone()
        print(h)
        
    conn.close()


c()
# # checking user data
# def d():
#     conn = sqlite3.connect('regn.db')
#     c = conn.cursor()
#     c.execute("SELECT *FROM regn WHERE first_name=?", (name,))
#     data = c.fetchall()
#     print(data)
#
#     conn.commit()
#
#     conn.close()
# d()'''

list = ['A', 's', 'c', 'a', 'd']
name = []
nam = input('Enter name ')

for i in  nam:
    name.append(i)
    
if name == list:
    print("found")
else:
    print('not found')
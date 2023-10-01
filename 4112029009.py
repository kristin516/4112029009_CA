# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 11:13:01 2023

@author: minni
"""

import sqlite3
conn=sqlite3.connect('BBQ.db')
cursor=conn.cursor()
cursor.execute('''
              CREATE TABLE IF NOT EXISTS meat(
                  id INTERGER PRIMARY KEY,
                  name TEXT,
                  price INTERGER,
                  quantity INTERGER
              )
''')
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('chicken',30,5)")
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('beef',55,10)")
cursor.execute("INSERT INTO meat(name,price,quantity)VALUES('pork',40,15)")
conn.commit()
cursor.execute('SELECT* FROM meat')
meat=cursor.fetchall()
print('內容:')
for BBQ in meat:
    print(meat)
cursor.execute("UPDATE meat SET price=35.0 WHERE name='pork'")
cursor.execute("UPDATE meat SET quantity=30.0 WHERE name='chicken'")
conn.commit()
cursor.execute('SELECT* FROM meat')
meat=cursor.fetchall()
print('內容:')
for BBQ in meat:
    print(meat)
cursor.execute("DELETE FROM meat WHERE price=40.0")
conn.commit()
cursor.execute('SELECT* FROM meat')
meat=cursor.fetchall()
print('內容:')
for BBQ in meat:
    print(meat)
cursor.close()
conn.close()
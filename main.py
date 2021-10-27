from sqlite3.dbapi2 import Time
import sys
import os
import uuid 
import sqlite3

__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"
__item_file__ = f"{__db_location__}/item.db"
cur = ""

def init():
    if_exits = os.path.exists(__db_location__)
    if if_exits==False:
        os.makedirs(__db_location__)

def view():
    f = open(__session_file__,"r")
    username=f.readline()
    print(username)

def login(username):
    f = open(__session_file__,"w")
    f.write(username)
    f.close()

class Item:
    def __init__(self):
        if_exits = os.path.exists(__item_file__)

    def save(self):
        _data_={
            "id":Time,
            "name":self.name,
            "price":self.price,
            "sellingPrice":self.sellingPrice
        }
        conItem = sqlite3.connect(__item_file__)  
        cur = conItem.cursor()
        # cur.execute('''CREATE TABLE items
        #        (id text, name text,price real, sellingPrice real)''')
        cur.execute("INSERT INTO items (id,name,price,sellingPrice) VALUES (?,?,?,?)",(str(uuid.uuid1()),self.name,self.price,self.sellingPrice))
        conItem.commit()
        conItem.close()

    def getAll(self):
        conItem = sqlite3.connect(__item_file__)  
        cur = conItem.cursor()
        for row in cur.execute('SELECT * FROM items ORDER BY price'):
            print(row)
        conItem.commit()
        conItem.close()

def item_create(name,price,selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.sellingPrice =selling_price
    item.save()

def item_all():
    print("get all items...")
    item = Item()
    item.getAll()

def item_view(id):
    print("View item ",id)

if __name__=="__main__":
    arguments = sys.argv[1:]

    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]
    
    init()

    if section == "user":
        if command == "login":
           login(*params)    
        elif command == "view":
           view()  
    elif section == "item":
        if command == "create":
            item_create(*params)
        elif command == "all":
            item_all()
        elif command == "view":
            item_view(*params)
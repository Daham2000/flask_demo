import sys
import os
import json
import sqlite3

__db_location__ = "db"
__session_file__ = f"{__db_location__}/session.db"
__item_file__ = f"{__db_location__}/item.db"

def init():
    if_exits = os.path.exists(__db_location__)
    if if_exits==False:
        os.makedirs(__db_location__)
    con = sqlite3.connect(__session_file__)
    print(con)
    
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
        if if_exits:
            with open(__item_file__) as item_file:
                print(type(item_file.readline()))
        else:
            print("No file exit")
            

    def save(self):
        num_lines = sum(1 for line in open(__item_file__))
        num_lines = num_lines+1
        _data_={
            "id":num_lines,
            "name":self.name,
            "price":self.price,
            "sellingPrice":self.sellingPrice
        }
        with open(__item_file__,"a") as item_file:
            json.dump(_data_,item_file,indent=1)

def item_create(name,price,selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.sellingPrice =selling_price
    item.save()

def item_all():
    print("Item All")
    with open(__item_file__) as item_file:
        print(item_file.readline())

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
import sqlite3

conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shock(
    item_name text primary key,
    qty integer
    )
""")

conn.commit()

def add_item(name,qty):
    cursor.execute('select qty from shock where item_name = ?',(name,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('insert into shock (item_name,qty) values(?,?)',(name,qty))
        print(f"Item {name} is added in db")
        print(f"Current qty of {name} is {qty}")
        print(f"{50*"-"}")
    else:
        current_qty = row[0] + qty
        cursor.execute('update shock set qty = ? where item_name = ?',(current_qty,name))
        print(f"{qty} of {name} is added")
        print(f"Current qty of {name} is {current_qty}")
        print(f"{50*"-"}")

    conn.commit()

def sell_item(name,qty):
    cursor.execute('select qty from shock where item_name = ?',(name,))
    row = cursor.fetchone()
    if row is None:
        print(f"this item is not exist in our records,please add this item into our system \n Or check the item name")

    else:
        # cursor.execute('select qty from shock where item_name = ?',(name,))
        row = cursor.fetchone()
        next_qty = row[0] - qty
        if next_qty >= 0:
            cursor.execute('update shock set qty = ? where item_name = ?',(next_qty,name))
            print(f"{qty} of {name} is sold")
            print(f"Current qty of {name} is {next_qty}")
            print(f"{50*"-"}")
            conn.commit()
        else:
            print("insufficient shock")
            print(f"Availabily of {name} is only {row[0]}")

def list_shocks():
    cursor.execute('select * from shock')
    rows = cursor.fetchall()
    sn = 1
    print(f"{'Sno':<3}|{'Item':<20}|Qty")
    for tuple in rows:
        print(f"{sn:>3}|{tuple[0]:<20}|{tuple[1]}")
        sn = sn + 1



# add_item("cotton_saree",20)
# # sell_item(name="silk_saree",qty=100)

# list_shocks()

print("Enter 1 for Add item \nEnter 2 for Sold \nEnter 3 for View_shock_list")

while(1):
    ops = int(input("Select operation..."))
    if(ops == 1):
        item = input("Enter Item Name")
        qty = int(input("Enter Quantity"))
        add_item(item,qty)
        print("Enter 0 for Exit")

    elif(ops == 2):
        item = input("Enter Item Name")
        qty = int(input("Enter Quantity"))
        sell_item(item,qty)
        print("Enter 0 for Exit") 

    elif(ops == 3):
        list_shocks()
        print("Enter 0 for Exit") 

    elif(ops == 0):
        print("Bye bye")
        break
        
    else:
        print("invalid option...\nPlease select between 0 to 3")
def addqty(name,qty):
    old_qty = shock[name]
    shock[name] = old_qty + qty
    print(qty,name,"is added successfully")
    print("total",name,"quanty is",shock[name])

def add_item(name):
    shock[name] = 0
    print("new item",name,"is created")

def show_shock():
    for key in shock.keys():
        print(key,":",shock[key])

def sold(name,qty):
    if((shock[name] - qty) > 0):
        shock[name] = shock[name] - qty
        print(qty,"is of",name,"sold")
        print("balance shock of",name,"is",shock[name])

shock = {}

add_item("phone")
add_item("headphone")

addqty("phone",10)
addqty("headphone",5)

show_shock()

sold("phone",7)

show_shock()


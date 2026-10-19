shock = {}

def add_item(name,qty):
    if name not in shock:
        shock[name] = 0

    shock[name] = shock[name] + qty
    print(f"Current qty of {name} is {shock[name]}")

def sold(name,qty):
    if name not in shock:
        print(f"{name} is not existing in our records")
        return
    
    if((shock[name]-qty) >= 0):
        shock[name] = shock[name] - qty
        print(f"{qty} {name} -- sold out")
        print(f"Remaining qty of {name} is {shock[name]}")
    else:
        print("insufficient qty for this Item",name)

def view_shock():
    print("Total shock list")
    for key in shock.keys():
        print(f"{key}:{shock[key]}")


add_item("samsung phone",10)
add_item("vivo phone",20)

view_shock()

sold("samsung phone",3)
sold("vivo phone",4)
sold("samsung phone",10)
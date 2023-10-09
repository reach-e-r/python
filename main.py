weigh=int(input("weight; "))
unit= input("kg or lbs: ")

if unit.lower()=="kg":
    size=2*weigh
    print(f"You are {size} pounds" )
else:
    mass=weigh/2
    print(f"You are {mass} kilos")

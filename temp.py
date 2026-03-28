te=input("enter temperature(warm/cold):")
hu=input("enter humidity(dry/humid):")
if te=="warm":
    if hu=="dry":
        print("activity:play basketball")
    elif hu=="humid":
        print("activity:play tennis")
    else:
        print("invalid humidity")
elif te=="cold":
    if hu=="dry":
        print("activity:paly cricket")
    elif hu=="humid":
        print("activity:swim")
    else:
        print("invalid humidity")
else:
    print("invalid temperature")

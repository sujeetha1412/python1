ba=float(input("enter initial balance:"))
t=input("enter transaction type(deposit/withdraw):")
am=float(input("enter transaction amount:"))
if t=="deposit":
    if am>=100:
        print("amount deposited successfully")
        print("balance=",ba+am)
    else:
        print("amount does not deposited")
else:
    if ba>=1000 and am<=ba:
        print("amount withdraw successfully")
        print("balance=",ba-am)
    else:
        print("your account balance should ba atleast 1000,so withdraw accordingly")

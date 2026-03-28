import math
a=float(input("enter coefficient a:"))
b=float(input("enter coefficient b:"))
c=float(input("enter coefficient c:"))
if a==0:
    print("This is not a quadratic equation")
else:
    d=b**2-4*a*c
    if d>0:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        print("roots are real and distinct")
        print("root1=",root1)
        print("root2=",root2)
    elif d==0:
        root=-b/(2*a)
        print("roots are real and equal")
        print("root=",root)
    else:
        print("roots are imaginary")

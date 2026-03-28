sa=float(input("enter your salary:"))
l=int(input("enter the no.of days leave:"))
if l<=2:
    print("Salary=",sa)
else:
    print("Deduction=",(l-2)*500)
    print("salary=",sa-((l-2)*500))
[25bcs165@mepcolinux ex1]$cat pyramid.py
no=int(input("enter n:"))
for i in range(no):
    ch=chr(65+i)
    for j in range(i+1):
        print(ch,end=" ")
    print()

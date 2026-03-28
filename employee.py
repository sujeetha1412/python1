sa=float(input("enter your salary:"))
l=int(input("enter the no.of days leave:"))
if l<=2:
    print("Salary=",sa)
else:
    print("Deduction=",(l-2)*500)
    print("salary=",sa-((l-2)*500))

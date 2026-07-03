salary=int(input("Enter salary : "))
tax=0
if(salary<30000):
    tax=(5/100)*salary
elif(salary>=30000 and salary<=70000):
    tax=(15/100)*salary
else:
    tax=(25/100)*salary

print("Tax at your salary: ",tax)

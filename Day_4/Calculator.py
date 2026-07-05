def calculate(x,y,operation):
    ans=0
    if operation == '+':
        ans=x+y
    elif operation == '-':
        ans=x-y    
    elif operation == '/':
        ans=x//y
    elif operation == '*':
        ans=x*y
    else:
        return "invalid"
    return ans
    

x=int(input("Enter an number X: "))
y=int(input("Enter an number Y: "))
operation=input("Enter a operation(+,-,/,*) :")

print(calculate(x,y,operation))
#factorial 

def fact(n):
    ans=1
    while n!=0:
        ans=ans*n
        n=n-1   
    print(ans)

n=(int(input("Enter an number n : ")))
fact(n)
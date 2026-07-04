def Sum(n):
    sum=0
    i=0
    while i<=n:
        sum+=i
        i=i+1
    return sum

n=int(input("Enter a number n: "))
print(Sum(n))    

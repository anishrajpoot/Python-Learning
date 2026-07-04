# Write a function to return the sum of a digits of number n

def SumOfDigit(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    return sum

n=int(input("Enter a number n: "))
print(SumOfDigit(n))

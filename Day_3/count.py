# Write a function to return the the number of digits in a number n.

def CountNum(n):
    count=0
    
    while n!=0:
        n= n // 10
        count= count+1  
    return count  

n=int(input("enter a num n: "))
print(CountNum(n))


def PrintNoDevBy3And5(n):
    
    while n!=0:
        
        if n%3==0 and n%5==0:
            print(n)
        n-=1

n=int(input("Enter an number n : "))
PrintNoDevBy3And5(n)           
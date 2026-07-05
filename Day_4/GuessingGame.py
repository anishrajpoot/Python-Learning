
def GuessingGame(secretNo):
    while True:
        n=int(input("Enter Your Guess :"))

        if n>secretNo:
            print("Too High")
        elif n<secretNo:
            print("Too Low")
        else:
            print("Correct")
            break
      
    
secretNo=245
GuessingGame(secretNo)

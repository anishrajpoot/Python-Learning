# Write a Python program to continuously accept a number from the user and print whether it is
# **positive**, **negative**, or **zero**. The program should keep accepting input until the 
# user enters **"Quit"**, after which it should terminate.

while True:
    a=input("Enter a number(or Quit): ")

    if a=="Quit":
        break
    
    else:
        a=int(a)
        if a>0:
            print("Positive")
        elif a<0:
            print("Negative")
        else:
            print("Zero")

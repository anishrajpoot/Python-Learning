data= {"Anish":90,"Ritesh":67}
inputt=input("enter A or B or C or D :")
if inputt=='A':
    data["Rohit"]=0
    print("Rohit Added")
    
elif inputt=='B':
    data["Anish"]=97
    print("Anish ,marks updated to 97")
    
elif input=='C':
    if "Anish" in data:
        print("Anish marks",data["Anish"])
  

elif inputt=='D':
    print(data)
else:
    print("invalid input")
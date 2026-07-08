# Print unique characters and their count

String=input("Enter a string : ")

countUnique=0
for i in String:
    count=0
    for j in String:
        if i==j:
            count+=1
    
    if count<=1:
        print("Unique char are :",i)
        countUnique+=1

print("UniqueChar Count : ",countUnique)

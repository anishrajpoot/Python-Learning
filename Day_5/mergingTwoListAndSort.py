List1=[]
List2=[]
n=int(input("ENter length of List: "))

i=0
while i!=n:
    num=int(input("Enter number in List1: "))
    List1.append(num)
    i=i+1

i=0
while i!=n:
    num=int(input("Enter number in List2: "))
    List2.append(num)
    i=i+1

AddedList=List1 +List2

ans=sorted(AddedList)
print(ans)

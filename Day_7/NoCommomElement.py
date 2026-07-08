# List1=[5,2,0,9]
# sizeOfList1=len(List1)
# List2=[8,3,2,1,7]
# sizeOfList2=len(List2)

# sett=set(List1+List2)
# sizeOfSett=len(sett)
# sumofListSize=sizeOfList1+sizeOfList2

# if sumofListSize==sizeOfSett:
#     print("No common")

# else:
#     print("Common")


#Alternet Way using intersection

List1=[5,2,0,9]

List2=[8,3,2,1,7]
common=set(List1) & set(List2)

if len(common)==0:
    print("No common element")
else:
    print("Common element")
    
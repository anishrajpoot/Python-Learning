List1=[5,2,3,98,3,8,2,0]

seen=set()
duplicate=set()
for i in List1:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)

    
print(duplicate)

# t1=(5,2,8,1,46,8,9)

# t2=[]
# t3=[]
# for i in t1:
#     if i%2==0:
#         t2.append(i)

#     else:
#         t3.append(i)

# print(tuple(t2))
# print(tuple(t3))


#method2
t1=(5,2,8,1,46,8,9)
t2=[]
t3=[]

for i in t1:
    if i%2==0:
        t2+=(i,)
    else:
        t3+=(i,)

print(tuple(t2))
print(tuple(t3))
#first we create list then isnert elent then convert into tuple
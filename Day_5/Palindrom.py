word=input("Enter a word :")

left=0
right=len(word)-1
while left<right:
    if word[left]!=word[right]:
        print("Not a Palindrom")
        break
    left=left+1
    right=right-1
print("Palindrom")

    

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.review=[]

    
    def AddnewReview(self,review):
        self.review.append(review)

    def countReview(self):
        return len(self.review)

    def display(self):
        print(self.review)
        


b=Book("poem","anish")
b.AddnewReview("best book")
b.AddnewReview("easy to read")
print("Total Review: ",b.countReview())
b.display()


























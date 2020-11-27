mystring="race a cara"
newlist=[]
anotherlist=[]
#except_palidrome = letter + number + ignore cases + space
print(mystring.isalnum())
mylist=list(mystring)

for elements in mylist:
    elements=elements.lower()
    if elements.isalnum():
        newlist.append(elements)
print(newlist)

opp=newlist[::-1]
print(opp)

if newlist == opp:
  print("palindrome")
else:
  print("not palindrome")

    
        

        
    
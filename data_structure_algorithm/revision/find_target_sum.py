mylist = [5, 3, 5, 1, 8]
target_sum = 10
length=len(mylist)

myset = set()
################################################
## first method 
# for i in range(length):
#     placeholder = target_sum - mylist[i]
#     myset.add(placeholder)
#     if sum(myset) < target_sum:
#         print(mylist[i], placeholder)
################################################
## second  method 
for i in range(length):
    placeholder = target_sum - mylist[i]

    if placeholder in myset:
        print(placeholder, mylist[i])
    else:
        myset.add(mylist[i])
    
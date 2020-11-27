# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

my_str="loveleetcode"
my_list=list(my_str)
print(my_list)
new_list=[]
for i in my_list:
    if i not in new_list:
        my_list[i] = 1
    else:
        my_list[i] += 1
   
# print(new_list)

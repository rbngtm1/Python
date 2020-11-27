# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

string = "hello"
my_string_list=(list(string))
# reverse_string=my_string_list.reverse()
print(my_string_list)
for i in my_string_list:
    my_string_list.reverse()
print(my_string_list)
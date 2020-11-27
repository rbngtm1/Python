# Given a 32-bit signed integer, reverse digits of an integer.

my_int=123
my_list=list(str(my_int))

for i in my_list:
    my_list.reverse()
print("".join(my_list))
# for j in my_list:
#     print(j, end="")

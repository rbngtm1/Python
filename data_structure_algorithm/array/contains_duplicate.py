array = [1,2,3,4]
my_array = []
# for i in array:
#     if i not in my_array:
#         my_array.append(i)
# if array == my_array:
#     print('false')
# else:
#     print('true')

def myfunc():

    for i in range(len(array)):
        if array[i] in my_array:
            return True
        else:
            my_array.append(array[i])
    return False

a=myfunc()
print(a)
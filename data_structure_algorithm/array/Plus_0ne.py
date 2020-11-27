given_array = [1, 2, 3, 4, 5]
# length = len(given_array)-1
#print(length)
# for i in range(0, len(given_array)):
#     #print(i)
#     if i==length:
#         given_array[i]=given_array[i]+1
        
#     else:
#         given_array[i]=given_array[i]
# print(given_array)
############################################
mylastindex=(given_array[-1]+1)
print(mylastindex)
remaining_array=(given_array[:-1])
remaining_array.append(mylastindex)
print(remaining_array)

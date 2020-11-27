# Remove duplicates from a string 
# For example: Input: string = 'banana'
#               Output: 'ban'
##########################

given_string = 'banana apple'
my_list = list()
for letters in given_string:
    if letters not in my_list:
        my_list.append(letters)
print(my_list)
print (''.join(my_list))

## possile solution exist using set data structure but 
## set structure is disorder 
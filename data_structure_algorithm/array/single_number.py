# pick the single number. the number which is not duplicated.
my_array = [2,2,3,4,4,5,5]
array1=[]
array2=[]

for elements in my_array:
  if elements not in array1:
    array1.append(elements)
  else:
    array2.append(elements)
print(array1, array2)

result = list(set(array1)-set(array2))
print(result)
    


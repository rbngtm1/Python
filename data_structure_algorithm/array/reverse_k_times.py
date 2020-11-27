array = [1,2,3,4,5]
lenth_array=len(array)
k = int(input("No. of time to rotate given array: "))

if k < lenth_array:
    print(array[-k:])
    print(array[:-k])
    array = (array[-k:] + array[:-k])
else:
    print('Plese enter valid number within', lenth_array)
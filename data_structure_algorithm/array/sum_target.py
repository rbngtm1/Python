# given_array = [3, 7, 8, 2]

# target = 9
# length = len(given_array)
# j = 0
# for i in range(0, length ):
#     j-=1
#     if (given_array[i] < target and given_array[-i] == target - given_array[i] ):
#         print(i , -i)

# Python program to find if there are 
# two elements wtih given sum 
  
# function to check for the given sum 
# in the array 

arr = [1, 4, 45, 6, 10, 8] 
arr_size = len(arr)
sum = 16
# def printPairs(arr, arr_size, sum): 
      
# Create an empty hash set 
s = set() 
    
for i in range(0, arr_size): 
    temp = sum-arr[i] 
    if (temp in s): 
        print ("Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(temp) + ")")
    s.add(arr[i]) 
  
# driver program to check the above function 
# A = [1, 4, 45, 6, 10, 8] 
# n = 16
# printPairs(A, len(A), n) 

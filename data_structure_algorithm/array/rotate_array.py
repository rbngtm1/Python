print('hello world')
A = [1,2,3,4,5,6,7]
k = input('no. of time to rotate an array: ')
n = len(A)

if k<n:

  print(A)
  print(A[:-k] , 'A[:-k]')
  print(A[-k:] , 'A[-k:]')
  A_rotate = A[-k:]+A[:-k]
  print(A_rotate)
else:  
  print('please enter valid no. within ',n)



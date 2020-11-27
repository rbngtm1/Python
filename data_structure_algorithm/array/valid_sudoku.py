# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

###################################################
# from numpy import *
given_sudoku= [
  ["5","5",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
# m = print(range(len(given_sudoku)))

myset = set()
length=len(given_sudoku)
newset=set()

for i in range(0,length):
  row = given_sudoku[0][i]
  if row not in myset and row != '.':
      myset.add(row)
      print('false')
print(myset)




# for j in range(1, length+1):
#   newset.add(str(j))
# print(newset)
# # newset={'2','3'}

# for i in myset:
#   if myset not in newset:
#     newset.add(i)
# print(newset)

# i=0
# for j in range(0,(len(given_sudoku))):
#   if given_sudoku[i][j] not in myset:
    
#     # print('false')
#   # if given_sudoku[i][j] != '.':
#     myset.add(given_sudoku[i][j])
#     print(myset)
# print('true') 




#################################################

# def notInRow(arr, row):  
  
#     # Set to store characters seen so far.  
#     st = set()  
  
#     for i in range(0, 9):  
  
#         # If already encountered before,  
#         # return false  
#         if arr[row][i] in st:  
#             return False
  
#         # If it is not an empty cell, insert value  
#         # at the current cell in the set  
#         if arr[row][i] != '.':  
#             st.add(arr[row][i])  
      
#     return True
  
# # Checks whether there is any  
# # duplicate in current column or not.  
# def notInCol(arr, col):  
  
#     st = set()  
  
#     for i in range(0, 9):  
  
#         # If already encountered before, 
#         # return false  
#         if arr[i][col] in st: 
#             return False
  
#         # If it is not an empty cell, insert  
#         # value at the current cell in the set  
#         if arr[i][col] != '.':  
#             st.add(arr[i][col])  
      
#     return True
  
# # Checks whether there is any duplicate  
# # in current 3x3 box or not.  
# def notInBox(arr, startRow, startCol):  
  
#     st = set()  
  
#     for row in range(0, 3):  
#         for col in range(0, 3):  
#             curr = arr[row + startRow][col + startCol]  
  
#             # If already encountered before,  
#             # return false  
#             if curr in st:  
#                 return False
  
#             # If it is not an empty cell,  
#             # insert value at current cell in set  
#             if curr != '.':  
#                 st.add(curr)  
          
#     return True
  
# # Checks whether current row and current  
# # column and current 3x3 box is valid or not  
# def isValid(arr, row, col):  
  
#     return (notInRow(arr, row) and notInCol(arr, col) and
#             notInBox(arr, row - row % 3, col - col % 3))  
  
# def isValidConfig(arr, n):  
  
#     for i in range(0, n):  
#         for j in range(0, n):  
  
#             # If current row or current column or  
#             # current 3x3 box is not valid, return false  
#             if not isValid(arr, i, j):  
#                 return False
          
#     return True
  
# # Drivers code  
# if __name__ == "__main__": 
  
#     board = [[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],  
#              [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],  
#              [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],  
#              [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],  
#              [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],  
#              [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],  
#              [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],  
#              [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],  
#              [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]] 
          
#     if isValidConfig(board, 9):  
#         print("YES") 
#     else: 
#         print("NO") 
  
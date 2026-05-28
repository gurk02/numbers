# import library
import numpy as np

#
# 1 dimensional 10x1 matrix
#

a1 = np.arange(10)  # creates a rank 1 array (1 dimensional) 10 elements, a range from 0 to 9 
print(f"array1 ={a1}")           # think of a1 as a 10x1 matrix
print(f"array1 shape= {a1.shape}")     # to get shape of array

a2 = np.arange(0,10,2)  # creates a range from 0 to 9 step 2
print (f"array2= {a2}")

a3 = np.zeros(5)        # create an array with all 0s
print (f"array3= {a3}")              #   
print (f"array3 shape= {a3.shape}")        # (5,)


#
# 2 dimensional np.array(10,2) 10x2 array
#
a4 = np.zeros((2,3))    # array of rank 2 with all 0s, 2 rows and 3 columns
print(a4.shape)
print(a4)

a5 = np.full((2,3),8)
print(a5)

a6 = np.eye(4)      # 4x4 identity matrix, creates 2 D array 4,4 with ones on the diagonal and zeros elsewhere
print(a6)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

a7 = np.random.random((2,4))    # rank 2 array (2 rows 4 columns) with
                                # random values
                                # in the half open interval (0.0, 1.0)
print(a7)


## another way to create numpy array is to create it from python list like so

list1 = [1,2,3,4,5]
r1 = np.array(list1)    # rank 1 array
print(r1)

print(r1[0])
print(r1[1])


list2 = [6,7,8,9,0]
r2 = np.array([list1, list2])   # rank 2 array
print(r2)       
# [[1 2 3 4 5]
#  [6 7 8 9 0]]

print(r2.shape)    # (2, 5) - 2 rows, 5 columns
print(r2[0,0])      # 1
print(r2[0,1])      # 2
print(r2[1,0])      # 6

# Boolean indexing
print(r1>2)     # [False False True True True]

print(r1[r1>2])    # [3 4 5]

nums = np.arrange(20)   # create array [0 .. 19]
print(nums)


odd_num = nums[nums % 2 == 1]   # [ 1 2 5 7]
print(odd_num)

# arr1 = np.array([1, 2, 3])
# print(arr1)

# SLICING
original_arr = np.array([[1,2,3,4,5],
                         [4,5,6,7,8],
                         [9,8,7,6,5]])  # rank 2 array

print(original_arr)

# to extract last two rows and first two columns, use slicing

b1 = original_arr[1:3, :2]  # row 1 to 3 not inclusive and first 3 columns
print(b1)           # reference to original_arr (not a copy!)

# output: 
#  [[4 5 6]
#   [9 8 7]]
#

b2 = original_arr[-2:, -2:]
print(b2)

# output: 
#  [[7 8]
#   [6 5]]
#

# slicing returns a reference to oringal array 
b3 = original_arr[1:, 2:]

# output: 
#  [[6,7,8]
#   [7,6,5]]
#

b3[0,2] = 88
# output: 
#  [[6,7,88 ]
#   [7,6,5]]
#

print(original_arr)

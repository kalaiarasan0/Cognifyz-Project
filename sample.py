import numpy as np

# # Example numpy array
            #iteration
# y = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# x = np.array([
#     [
#         [1, 2, 3], [4, 5, 6],
#         [7, 8, 9], [10, 11, 12]
#     ],
#     [
#         [13, 14, 15], [16, 17, 18],
#         [19, 20, 21], [22, 23, 24]
#     ]
# ])

            # Iterate over the array
# for i in range(x.shape[0]):
    
#     for j in range(x.shape[1]):
        
#         for k in range(x.shape[2]):
#             print(x[i][j][k])


# # Reshape 'x' to 2 rows and 3 columns
# # x_reshaped = x.reshape((2,2,3))

# # for j in x:
# #     for d in j:
# #         for f in d:
# #             for e in f:
# #                 print(e,end=" ")
                
# for n in np.nditer(x):
#     print(n)

            #join () and split()

# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]])
# arr = np.array([
#     [
#         [1, 2, 3], [4, 5, 6],
#         [7, 8, 9], [10, 11, 12]
#     ],
#     [
#         [13, 14, 15], [16, 17, 18],
#         [19, 20, 21], [22, 23, 24]
#     ]
# ])
# newarr = np.dsplit(arr, 3)
# print(newarr)


            #search()

# x = np.array([1,2,3,4,5,3,4,8,9])
# # y = np.where(x == 3)
# y = np.where(x%2 == 0)
# # output
# #(array([1, 3, 6, 7], dtype=int64),)
# print(y)
            #seachsorted()
# x = np.array([[1,2,3,4,5,3,4,8,9],
#               [1,2,3,86,2,3,8,782,2]])
# x = np.array([1,2,3,4,5,3,4,8,9])
# y = np.searchsorted(x, 1000)
# print(y)

# Create a 2D array
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# # Flatten the array
# arr_flat = arr.flatten()
# # Sort the flattened array
# arr_flat_sorted = np.sort(arr_flat)
# # Perform searchsorted
# indices = np.searchsorted(arr_flat_sorted, 4)
# # Reshape the indices to match the original array shape
# indices_2d = np.unravel_index(indices, arr.shape)
# print("Indices where 4 should be inserted to maintain order:", indices_2d)
# print(indices)


            #Sort()
            #2-D
# arr = np.array([[1, 2, 3],
#                 [7, 14, 9],
#                 [4, 5, 6]])
# print(np.sort(arr))

                #Filter()
# arr = np.array([31,32,33,34])
# fil_arr = []
# for x in arr:
#     if not x > 32:
#         fil_arr.append(False)
#     else:
#         fil_arr.append(True)
# newarr = arr[fil_arr]
# print(fil_arr)
# print(newarr)
arr = np.array([31,32,33,34])
fil_arr = arr%2 == 1
newarr = arr[fil_arr]
print(fil_arr)
print(newarr)
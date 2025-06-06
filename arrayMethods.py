from array import *

# 1. Create an integer array
arr = array('i', [10, 20, 30, 40, 50])
print("Original array:", arr)

# 2. Access elements by index
print("Element at index 2:", arr[2])

# 3. Append element
arr.append(60)
print("After append(60):", arr)

# 4. Insert element at index
arr.insert(2, 25)
print("After insert(2, 25):", arr)

# 5. Remove element by value
arr.remove(30)
print("After remove(30):", arr)

# 6. Pop element (last one)
popped = arr.pop()
print("After pop():", arr, "| Popped:", popped)

# 7. Index of element
index_val = arr.index(40)
print("Index of 40:", index_val)

# 8. Reverse the array
arr.reverse()
print("After reverse():", arr)

# 9. Slice array
sliced = arr[1:4]
print("Sliced array [1:4]:", sliced)

# 10. Loop through array
print("Looping through array:")
for i in arr:
    print(i, end=' ')
print()

# 11. Length of array
print("Length of array:", len(arr))

# 12. Convert array to list
arr_list = arr.tolist()
print("Converted to list:", arr_list)

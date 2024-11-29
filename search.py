# # Linear Search
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index where the target is found
#     return -1  # Return -1 if the target is not found

# # Example usage
# arr = [10, 20, 30, 40, 50]
# target = 30

# result = linear_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")










# # Binary Search
# def binary_search(arr, target):
#     low = 0  # Starting index of the list
#     high = len(arr) - 1  # Ending index of the list
    
#     while low <= high:
#         mid = (low + high) // 2  # Find the middle index
        
#         if arr[mid] == target:
#             return mid  # Target found, return the index
        
#         elif arr[mid] < target:
#             low = mid + 1  # Target is in the right half, so move the low pointer
#         else:
#             high = mid - 1  # Target is in the left half, so move the high pointer
            
#     return -1  # Target not found

# # Example usage
# arr = [10, 20, 30, 40, 50, 60, 70]
# target = 40

# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")












# Recursive Binary Search Code:
def recursive_binary_search(arr, target, low, high):
    # Base case: If low index is greater than high index, the target is not found
    if low > high:
        return -1
    
    # Find the middle index
    mid = (low + high) // 2
    
    # If the target is found at the middle index
    if arr[mid] == target:
        return mid
    
    # If the target is smaller than the middle element, search the left half
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    
    # If the target is greater than the middle element, search the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

# Example usage
arr = [10, 20, 30, 40, 50, 60, 70]
target = 40

# Call the recursive binary search with the initial low and high indices
result = recursive_binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")





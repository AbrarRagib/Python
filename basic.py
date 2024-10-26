# 1. Find the Largest Number in an Array
# Problem: Write a function to find the largest number in a given array.

# def find_largest(arr):
#     if len(arr) == 0:
#         return None
#     largest = arr[0]
#     for num in arr:
#         if num > largest:
#             largest = num
#     return largest
    
# arr = [3,5,4,6,8,9]
# print(find_largest(arr))

# #smallest number in array

# def find_smallest(arr):
#     if len(arr) == 0:
#         return None
#     smallest = arr[0]
#     for num in arr:
#         if num < smallest:
#             smallest = num
#     return smallest


# # Example usage:
# arr = [3, 5, 4, 6, 8, 9]
# print(find_smallest(arr))  # Output: 3


# Check the middle value in an array (or list) in Python

# def get_middle_value(arr):
#     if len(arr) == 0:
#         return None  # Return None if the array is empty
    
#     mid_index = len(arr) // 2  # Calculate the middle index
    
#     # Check if the length is odd or even
#     if len(arr) % 2 == 1:
#         # Odd length: return the middle element
#         return arr[mid_index]
#     else:
#         # Even length: return the two middle elements
#         return arr[mid_index - 1], arr[mid_index]

# # Example usage:
# arr1 = [1, 3, 5, 7, 9]
# print(get_middle_value(arr1))  # Output: 5 (middle element)

# arr2 = [2, 4, 6, 8]
# print(get_middle_value(arr2))  # Output: (4, 6) (two middle elements)




# 2. Check for Palindrome String
# Problem: Write a function to check whether a string is a palindrome or not (reads the same forward and backward).



# def is_palindrome(s):
#     # Check if the string 's' is equal to its reverse.
#     # s[::-1] reverses the string 's' by slicing it from end to start.
#     return s == s[::-1]
# # s[::-1]: This is a slicing technique that reverses the string s. The syntax [start:stop:step] allows control over slicing. Here, step = -1 means slice the string backward, effectively reversing it.

# # Example usage:
# # Test if "madam" is a palindrome
# print(is_palindrome("madam"))  # Output: True, because "madam" is the same forward and backward.

# # Test if "hello" is a palindrome
# print(is_palindrome("hello"))  # Output: False, because "hello" is not the same forward and backward.








# # 2nd way
# # Write a function to check if a given string is a palindrome.``
# def is_palindrome(s):
#     # Convert to lowercase and remove spaces
#     s = s.replace(" ", "").lower()
# #     s.replace(" ", "") removes all spaces in the string s by replacing each space character (" ") with an empty string ("").
# # .lower() converts all characters in the string to lowercase.
#     # Compare string with its reverse
#     return s == s[::-1] 
# # s[::-1]: This is a slicing technique that reverses the string s. The syntax [start:stop:step] allows control over slicing. Here, step = -1 means slice the string backward, effectively reversing it. -1 means backwards and 1 means forwards(check the same line)

# # Example usage:
# print(is_palindrome("A man a plan a canal Panama"))  # Output: True
# print(is_palindrome("hello"))  # Output: False




# def is_palindrome(s):
#     s = s.replace(" ","").lower()
#     return s == s[::-1]



# print('Output is: ',is_palindrome("A man a plan a canal Panama"))





# 3. FizzBuzz Problem
# Problem: Print numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."


# def fizz_buzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# # Example usage:
# fizz_buzz()




# 4. Find Duplicate Elements in an Array
# Problem: Write a function to find duplicate elements in a given array.


# def find_duplicates(arr):
#     duplicates = []
#     seen = set()
#     for num in arr:
#         if num in seen:
#             duplicates.append(num)
#         else:
#             seen.add(num)
#     return duplicates

# # Example usage:
# arr = [1, 2, 3, 4, 5, 2, 3, 6]
# print(find_duplicates(arr))  # Output: [2, 3]




# 5. Reverse an Array
# Problem: Write a function to reverse a given array.



# def reverse_array(arr):
#     return arr[::-1]

# # Example usage:
# arr = [1, 2, 3, 4, 5]
# print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]





# 6. Count Vowels in a String
# Problem: Write a function to count the number of vowels in a given string.


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
print(count_vowels("hello world"))  # Output: 3


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1 
    return count

print(count_vowels('ragib'))




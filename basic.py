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




# 4. Find Duplicate Elements in an Array ***
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


# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# # Example usage:
# print(count_vowels("hello world"))  # Output: 3






# def count_con(s):
#     cons = "bcdfghjklmnpqrstvzxyz"
#     count = 0
#     for char in s:
#         if char in cons:
#             count += 1
#     return count
# print(count_con('abrar ragib'))



# 7. Sum of Even Numbers in an Array
# Problem: Write a function to calculate the sum of all even numbers in a given array.


# def sum_of_evens(arr):
#     return sum(num for num in arr if num % 2 == 0)

# # Example usage:
# arr = [1, 2, 3, 4, 5, 6]
# print(sum_of_evens(arr))  # Output: 12



# #my way:
# def sum_of_even(arr):
#     add = 0
#     for num in arr:
#         if num % 2 == 0:
#             add += num
#     return add
    

# arr= [1,2,3,4,4]
# print(sum_of_even(arr))









# 8.Anagram Problem ***
# Problem: Write a function that checks if two strings are anagrams of each other. Two strings are considered anagrams if they contain the same characters in the same frequency but in any order. For example, "listen" and "silent" are anagrams.




# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if both strings have the same length
#     if len(str1) != len(str2):
#         return False

#     # Sort both strings and compare
#     return sorted(str1) == sorted(str2)

# # Example usage:
# print(are_anagrams("listen", "silent"))  # Output: True
# print(are_anagrams("triangle", "integral"))  # Output: True
# print(are_anagrams("hello", "world"))  # Output: False


# # mine:
# def are_anagrams(str1, str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()
    
#     if len(str1)  != len(str2):
#         return False
#     return sorted(str1) == sorted(str2)

# print(are_anagrams('listen', 'silent'))




# 9. Check if Two Strings are Permutations of Each Other
# Problem: Write a function to check if two strings are permutations of each other. Two strings are permutations if they have the same characters in the same frequency, but they do not need to be in order.

# def are_permutations(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if the strings have the same length
#     if len(str1) != len(str2):
#         return False

#     # Use a dictionary to count occurrences of each character
#     char_count = {}
#     for char in str1:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     for char in str2:
#         if char not in char_count:
#             return False
#         char_count[char] -= 1
#         if char_count[char] < 0:
#             return False

#     return True

# # Example usage:
# print(are_permutations("abc", "bca"))  # Output: True
# print(are_permutations("abc", "bcd"))  # Output: False








# # 10. Longest Palindromic Substring ---
# # Problem: Write a function to find the longest palindromic substring in a given string.

# def longest_palindrome(s):
#     def expand_around_center(s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left+1:right]

#     result = ""
#     for i in range(len(s)):
#         # Odd length palindromes
#         temp = expand_around_center(s, i, i)
#         if len(temp) > len(result):
#             result = temp
#         # Even length palindromes
#         temp = expand_around_center(s, i, i+1)
#         if len(temp) > len(result):
#             result = temp

#     return result

# # Example usage:
# print(longest_palindrome("babad"))  # Output: "bab" or "aba"
# print(longest_palindrome("cbbd"))   # Output: "bb"



# 11. Check if Two Strings are Rotations of Each Other
# Problem: Write a function to check if one string is a rotation of another string. For example, "waterbottle" is a rotation of "erbottlewat."



# def are_rotations(str1, str2):
#     # If lengths are not the same, they can't be rotations
#     if len(str1) != len(str2):
#         return False
#     # Concatenate the first string to itself and check if the second string is a substring of it
#     return str2 in str1 + str1

# # Example usage:
# print(are_rotations("waterbottle", "erbottlewat"))  # Output: True
# print(are_rotations("hello", "llohe"))              # Output: True
# print(are_rotations("hello", "world"))              # Output: False



# # another way:

# def are_rotations(str1, str2):
#     # Step 1: Check if lengths are equal, if not, return False
#     if len(str1) != len(str2):
#         return False
    
#     # Step 2: Concatenate str1 with itself
#     combined = str1 + str1
    
#     # Step 3: Check if str2 is a substring of combined
#     return str2 in combined

# # Example usage:
# print(are_rotations("waterbottle", "erbottlewat"))  # Output: True
# print(are_rotations("hello", "llohe"))              # Output: True
# print(are_rotations("hello", "world"))              # Output: False





# 4. Remove Duplicate Characters in a String ***
# Problem: Write a function that removes duplicate characters in a given string.


def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)

# Example usage:
print(remove_duplicates("aabbcc"))  # Output: "abc"
print(remove_duplicates("abracadabra"))  # Output: "abrcd"


#Dub_Number find in array:
def find_duplicates(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Example usage:
arr = [1, 2, 3, 4, 5, 2, 3, 6]
print(find_duplicates(arr))  # Output: [2, 3]
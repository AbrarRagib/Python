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





# 12. Remove Duplicate Characters in a String ***
# Problem: Write a function that removes duplicate characters in a given string.


# def remove_duplicates(s):
#     seen = set()
#     result = []
#     for char in s:
#         if char not in seen:
#             result.append(char)
#             seen.add(char)
#     return ''.join(result)

# # Example usage:
# print(remove_duplicates("aabbcc"))  # Output: "abc"
# print(remove_duplicates("abracadabra"))  # Output: "abrcd"


# #Dub_Number find in array:
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












# # 13. Find the First Non-Repeating Character in a String
# # Problem: Write a function to find the first non-repeating character in a string. If all characters repeat, return None.

# def first_non_repeating_char(s):
#     char_count = {}  # Step 1: Dictionary to count characters
    
#     # Count each character's frequency
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     # Find the first character with a count of 1
#     for char in s:
#         if char_count[char] == 1:
#             return char
    
#     # If no non-repeating character found, return None
#     return None


# # Example usage:
# print(first_non_repeating_char("abracadabra"))  # Output: "c"
# print(first_non_repeating_char("aabbcc"))  # Output: None












# 14. Check if a String is a Valid Number
# Problem: Write a function to check if a given string represents a valid number (integer or floating-point).



# def is_valid_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False

# # Example usage:
# print(is_valid_number("123"))      # Output: True
# print(is_valid_number("123.45"))   # Output: True
# print(is_valid_number("123abc"))   # Output: False



# 15. Check if a String has All Unique Characters
# Problem: Write a function to determine if a string has all unique characters, without using additional data structures.

# def has_unique_chars(s):
#     # Assuming the string contains ASCII characters (256 possible characters)
#     if len(s) > 256:
#         return False

#     char_set = [False] * 256
#     for char in s:
#         if char_set[ord(char)]:
#             return False
#         char_set[ord(char)] = True
#     return True

# # Example usage:
# print(has_unique_chars("abcde"))  # Output: True
# print(has_unique_chars("aabbcc")) # Output: 












# 16. Count the Frequency of Characters in a String
# Problem: Write a function that counts the frequency of each character in a string and returns a dictionary.



# def char_frequency(s):
#     freq_dict = {}
#     for char in s:
#         freq_dict[char] = freq_dict.get(char, 0) + 1
#     return freq_dict

# # Example usage:
# print(char_frequency("abracadabra"))  
# # Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}













# 17. Write a Python function that determines if two strings are isomorphic.***

# Example Input: "egg", "add"
# Example Output: True (because 'e' maps to 'a' and 'g' maps to 'd' consistently)
# Example Input: "foo", "bar"
# Example Output: False (because 'o' maps to two different letters)




# def is_isomorphic(s, t):
#     if len(s) != len(t):
#         return False
    
#     # Two dictionaries to store the character mappings from s to t and t to s
#     mapping_s_t = {}
#     mapping_t_s = {}
    
#     for char_s, char_t in zip(s, t):
#         # Check the s -> t mapping
#         if char_s in mapping_s_t:
#             if mapping_s_t[char_s] != char_t:
#                 return False
#         else:
#             mapping_s_t[char_s] = char_t
        
#         # Check the t -> s mapping
#         if char_t in mapping_t_s:
#             if mapping_t_s[char_t] != char_s:
#                 return False
#         else:
#             mapping_t_s[char_t] = char_s

#     return True

# # Test cases
# print(is_isomorphic("egg", "add"))  # Output: True
# print(is_isomorphic("foo", "bar"))  # Output: False
# print(is_isomorphic("paper", "title"))  # Output: True




# # easy:
# def is_isomorphic(s, t):
#     # The idea is to use two sets to verify unique mappings between characters in s and t
#     return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

# # Test cases
# print(is_isomorphic("egg", "add"))    # Output: True
# print(is_isomorphic("foo", "bar"))    # Output: False
# print(is_isomorphic("paper", "title")) # Output: True















# 18. Write a Python function that takes a string as input and returns a dictionary containing all the characters that appear more than once in the string along with their respective counts. If there are no repeated characters, the function should return an empty dictionary. ***


# def find_repeated_chars(s):
#     # Dictionary to store character counts
#     char_count = {}
    
#     # Count occurrences of each character
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     # Collect characters that have a count greater than 1
#     repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    
#     return repeated_chars

# # Test cases
# print(find_repeated_chars("programming"))  # Output: {'r': 2, 'g': 2, 'm': 2}
# print(find_repeated_chars("hello world"))  # Output: {'l': 3, 'o': 2}











# 19. Write a Python function that checks if a given phone number is a valid Bangladeshi phone number. The function should return True if the number is valid, and False otherwise. ***DSI



# import re

# def is_valid_bd_number(phone_number):
#     # Define regular expressions for 11-digit national format and 13-digit international format with +880
#     pattern_11_digits = r"^(013|014|015|016|017|018|019)\d{8}$"      # For 11-digit numbers
#     pattern_13_digits = r"^\+880(13|14|15|16|17|18|19)\d{8}$"       # For 13-digit numbers with +880

#     # Check if the phone number matches either pattern
#     if re.match(pattern_11_digits, phone_number) or re.match(pattern_13_digits, phone_number):
#         return True
#     return False

# # Test cases
# print(is_valid_bd_number("01712345678"))  # True - 11-digit number
# print(is_valid_bd_number("+8801712345678"))  # True - 13-digit number with +880
# print(is_valid_bd_number("019123456"))  # False - not enough digits
# print(is_valid_bd_number("02123456789"))  # False - invalid prefix
# print(is_valid_bd_number("+880141234567"))  # False - not enough digits








# 20. Two strings, s and t, are called isomorphic if the characters in s can be replaced to get t, preserving the order of characters. However, each character in s must map to a unique character in t. ***DSI



# def is_isomorphic(s, t):
#     if len(s) != len(t):
#         return False

#     # Two dictionaries to store mappings
#     mapping_s_t = {}
#     mapping_t_s = {}

#     for char_s, char_t in zip(s, t):
#         # Check s -> t mapping
#         if char_s in mapping_s_t:
#             if mapping_s_t[char_s] != char_t:
#                 return False
#         else:
#             mapping_s_t[char_s] = char_t

#         # Check t -> s mapping
#         if char_t in mapping_t_s:
#             if mapping_t_s[char_t] != char_s:
#                 return False
#         else:
#             mapping_t_s[char_t] = char_s

#     return True

# # Test cases
# print(is_isomorphic("egg", "add"))  # Output: True
# print(is_isomorphic("foo", "bar"))  # Output: False
# print(is_isomorphic("paper", "title"))  # Output: True
# print(is_isomorphic("ab", "aa"))  # Output: False
















# 21. Write a function that checks if a given string is an isogram. The function should return True if the string is an isogram and False otherwise. For simplicity, ignore letter case and ignore spaces or hyphens. ***DSI



def is_isogram(word):
    # Convert to lowercase to ignore case
    word = word.lower()
    
    # Use a set to store characters we encounter
    seen = set()
    
    for char in word:
        # Ignore spaces and hyphens
        if char in (' ', '-'):
            continue
        # If character is already in set, it's a duplicate
        if char in seen:
            return False
        seen.add(char)
    
    # If we complete the loop without duplicates, it's an isogram
    return True

# Test cases
print(is_isogram("machine"))          # Output: True
print(is_isogram("programming"))      # Output: False
print(is_isogram("Dermatoglyphics"))  # Output: True
print(is_isogram("hello-world"))      # Output: False
print(is_isogram("isogram"))          # Output: True


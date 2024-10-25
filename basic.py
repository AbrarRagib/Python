# 1. Find the Largest Number in an Array
# Problem: Write a function to find the largest number in a given array.

def find_largest(arr):
    if len(arr) == 0:
        return None
    largest = arr[0]
    for num in arr:
        if num
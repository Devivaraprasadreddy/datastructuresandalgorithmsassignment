# Approach 3 - 

# User-defined function - Create a function - “check_ele” which will find the duplicate element in the array and display the occurrence of the duplicate element in the terminal.

# Sample Input - [2, 3, 1, 2, 5, 7, 2, 3, 5]

# Sample Output - The frequency of “2” element is - 3

# The frequency of “3” element is - 2

# The frequency of “5” element is - 2






def check_ele(arr, n, ele):
    count = 0
    for i in range(n):
        if arr[i] == ele:
            count += 1
    return count

def find_freq(arr, n):
    for i in range(n):
        count = check_ele(arr, n, arr[i])
        if count > 1:
            print("The frequency of", arr[i], "element is", count)

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
n = len(arr)
find_freq(arr, n)
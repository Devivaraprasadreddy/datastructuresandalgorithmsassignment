# Approach 1 - 

# Recursive Function - A function that calls itself is known as a recursive function. Declare a function - “dup_ele()” which will find the frequency of duplicate elements from the array and display it individually. We need to count the duplicate elements in the array. This function - “dup_ele()” is a recursive function that will call itself in the code. 


# Sample Input - [2, 3, 1, 2, 5, 7, 2, 3, 5]

# Sample Output - The frequency of “2” element is - 3

# The frequency of “3” element is - 2

# The frequency of “5” element is - 2


def dup_ele(arr, n, index, ele, freq):
    if index == n:
        return
    if arr[index] == ele:
        freq[0] += 1
    dup_ele(arr, n, index + 1, ele, freq)

def find_freq(arr, n):
    for i in range(n):
        freq = [0]
        dup_ele(arr, n, 0, arr[i], freq)
        if freq[0] > 1:
            print("The frequency of", arr[i], "is", freq[0])

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
n = len(arr)
find_freq(arr, n)
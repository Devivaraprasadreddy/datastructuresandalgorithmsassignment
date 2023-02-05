# Approach 2 -

# Iterative Method - Here,  we need to write simple code to figure out the duplicate entries of the element by traversing the array. In every iteration, we need to check the elements for duplication purposes. We need to count the frequency of the duplicate elements and display the output for each duplicate entries. 

# Sample Input - [2, 3, 1, 2, 5, 7, 2, 3, 5]

# Sample Output - The frequency of “2” element is - 3

# The frequency of “3” element is - 2

# The frequency of “5” element is - 2


def find_freq(arr, n):
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                count += 1
        if count > 1:
            print("The frequency of", arr[i], "is", count)

arr = [2, 3, 1, 2, 5, 7, 2, 3, 5]
n = len(arr)
find_freq(arr, n)
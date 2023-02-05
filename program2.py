

# Write a program (W.A.P) to find out the unique elements in the array by implementing the sorting technique. 


# Sample Input - [5, 4, 7, 5, 1, 3, 4]

# Sample Output - [1, 3, 4, 5, 7]

#  removing the duplicate elements in an array


a = []
n = int(input("Enter the number of elements: "))
for x in range(0,n):
    element= int(input('Enter the elements : '+str(x+1)+" :"))
    a.append(element)
b = set() 
unique = []
for x in a :
    if x not in b:
        unique.append(x)
        b.add(x)
        unique.sort()
print("Unique elements in the array are : ",unique)   
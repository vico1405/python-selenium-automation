'''# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
# arr = [5,7,23,15,1,0,30]

arr = [5, 7, 23, 15, 1, 0, 30]
# sort in descending order
arr.sort(reverse=True)
print(arr)


# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


arr = [5, 7, 23, 15, 1, 0, 30]
bubbleSort(arr)

print(arr)

# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.
# code to get list

B = []
C = int(input("Enter the size of list:"))
print("Enter the element one by one:")

for i in range(C):
    D = int(input("->"))
    B.append(D)

print("The given list is:")
print(B)

# To perform insertion sort.
for i in range(1, len(B)):
    key = B[i]
    j = i - 1
    while j >= 0 and key > B[j] :
        B[j + 1] = B[j]
        j -= 1
    B[j + 1] = key

print("List after sorting:\n", B)'''

arr = [5, 7, 23, 15, 1, 0, 30]
# sort in descending order
arr.sort(reverse=True)
print(arr)

# implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        # finding the mid array
        mid = len(arr)//2

        # splitting the array to equal halves
        L = arr[:mid]
        R = arr[mid:]

        # sorting L
        mergeSort(L)
        # Sorting R
        mergeSort(R)

        i = j = k = 0
        # copy data to temp arrays L[] and R[]
        while i < len(L) and J < len(R):
            if L[i] < R[i]:
                i += 1
            else:
                arr[k] = R[j]
                j  += 1
                k += 1
        # checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        # To print list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
# Driver code

    arr = [5, 7, 23, 15, 1, 0, 30]
    print("Given array is")
    printList(arr)
    print("\n")
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    print(mergeSort(arr))



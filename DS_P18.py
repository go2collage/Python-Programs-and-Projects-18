# Python Program / Project

def radixsort(arr):
    maxElement = max(arr)
    place = 1
    while maxElement // place > 0:
        countingsort(arr, place)
        place = place * 10

def countingsort(arr, place):
    n = len(arr)
    result = [0] * n
    cnt = [0] * 10      # count variable

    # calculate count of element based on digit place
    i = 0
    for i in range(n):
        index = int(arr[i]) // place
        cnt[index % 10] += 1

    for i in range(1, 10):
        cnt[i] = cnt[i] + cnt[i-1]

    # place elements in sorted order
    i = n - 1
    while i >= 0:
        index = int(arr[i]) // place
        result[cnt[index%10] - 1] = arr[i]
        cnt[index % 10] -= 1
        i = i - 1
    
    # place back the sorted elements in original 
    for i in range(0, n):
        arr[i] = result[i]


# Driver Code

num = int(input("How many students in training program: "))
arr = []

i = 0
for i in range(num):
    item = float(input("Enter percentage marks: "))
    arr.append(item)

print("You have entered following percentage marks: ")
print(arr)

radixsort(arr)
print("The sorted list using Radix Sort is: ")
print(arr)

print("Top five percentage marks: ")
for i in range(len(arr)-1, 1, -1):
    print(arr[i])


def nextGreatest(arr):
    size = len(arr)
    max_from_right = arr[size - 1]
    arr[size - 1] = -1
    for i in range(size - 2, -1, -1):
        temp = arr[i]
        arr[i] = max_from_right
        if max_from_right < temp:
            max_from_right = temp

def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i],end=' ')

arr=[]
n=int(input("Enter the length of array:"))
for i in range(n):
    ele=int(input())
    arr.append(ele)

nextGreatest(arr)
print("Modified array is")
printArray(arr)

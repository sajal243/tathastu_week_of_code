lst = list(tuple(map(int, input().split())) for i in range(int(input("Enter no.of rows:"))))
n= int(input("Enter the nth element to sort:"))
print(lst)
lst.sort(key=lambda x:x[n])
print(lst)
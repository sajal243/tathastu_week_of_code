def spc_sorting(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        if(i%2!=0):
            lst1.append(i)
        else:
            lst2.append(i)

    return (sorted(lst1,reverse=True)+sorted(lst2))


lst = []
n = int(input("Enter the length of list:"))
for i in range(n):
    lst.append(int(input()))

print(spc_sorting(lst))

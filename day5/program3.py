def stolen(lst):
    if(len(lst)==2):
        return max(lst)
    if(len(lst)==1):
        return lst[0]
    if(len(lst)==3):
        return max(lst[0]+stolen(lst[2:]),lst[1])
    return max(lst[0]+stolen(lst[2:]),lst[1]+stolen(lst[3:]))

lst=[]
n=int(input("Enter the length of list:"))
for i in range(n):
    lst.append(int(input("Enter the value in house" + str(i+1) + ':')))

print("max. stolen value is:",stolen(lst))

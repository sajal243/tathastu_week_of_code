lst1 = list(map(int, input("Enter the list1 items:").split()))
maxx = sum(lst1)
lst2 =[]

from itertools import combinations
for i in range(2,max(lst1)+1):
    comb= combinations(lst1,i)
    for i in list(comb):
        lst2.append(sum(i))


for i in range(1,maxx):
    if ((i not in lst1) and (i not in lst2)):
        print(i)
        break

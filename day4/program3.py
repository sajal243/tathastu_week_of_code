n= int(input("Enter the no. of keys:"))
dic= dict( input().split() for i in range(n))
print(dic)
print(list(sorted(dic.values()))[-2])

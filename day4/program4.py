n= int(input("Enter the no. of keys:"))
dic = dict(input().split() for i in range(n))
print(dic)
d={}
for key,value in dic.items():
    if value not in d:
        d[key]=value

print(d)

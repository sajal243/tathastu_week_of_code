def knapsack(wgt,lst):
    if(wgt==0 or len(lst)==0):
        return 0
    if(len(lst)==1):
        if(lst[0][0]>wgt):
            return 0
        return lst[0][1]

    if(lst[0][0]>wgt):
        return knapsack(wgt,lst[1:])
    return max(lst[0][1]+knapsack(wgt-lst[0][0],lst[1:]),knapsack(wgt,lst[1:]))

    

n=int(input("total items u have:"))
lst=[]

for i in range(n):
    wgt=int(input("Enter weight of"+str(i)+"item:"))
    value= int(input("Enter value of" +str(i)+ "nd item:"))
    lst.append((wgt,value))

wgt = int(input("Enter the value of weight capacity: "))
print("The maximum value for the given weight value pair is ", knapsack(wgt, lst))

tup = input("Enter the elements in the tuples:")
x= input('Enter the elements whose occurence u wanna count:')
count=0
for i in tup:
    if(x==i):
        count+=1

print("Occurence of element is:",count)

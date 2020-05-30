votes=int(input("Enter the no. of votes:"))
candi=[]
for i in range(votes):
    candi.append(input("Enter the name of candidate:"))

vote=[]
for i in candi:
    vote.append((i,candi.count(i)))

vote.sort(key=lambda x:x[0],reverse=True)
vote.sort(key=lambda x:x[1])

print("the winning candidate is:",vote[-1][0])

def charCount(word):
    dict = {}
    for i in word:
        dict[i]=dict.get(i,0) +1
    return dict

def possible(lst, arr):
    for word in lst:
        flag=1
        chars = charCount(word)
        for key in chars:
            if key not in arr:
                flag=0
            elif(arr.count(key) != chars[key]):
                flag=0

        if(flag==1):
            print(word)

if(__name__=="__main__"):
    '''lst = input("Enter the words in the list:")
    n = int(input("Enter size of array:"))
    arr = []
    for _ in range(n):
        arr.append(input())'''
    lst=['go','bat','me','eat','goal','boy','run']
    arr=['e','o','b','a','m','g','l']

    possible(lst,arr)

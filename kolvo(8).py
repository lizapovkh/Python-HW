a=[2, 5, 7, 3, 8, 1, 4, 7, 2, 0]
b=[]
c=0
for i in range (1,len(a)):
    if a[i-1]<a[i]:
        c+=1
print(c)

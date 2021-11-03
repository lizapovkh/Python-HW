a=[2, 5, 7, 3, 8, 1, 4, 7, 2, 0]
c=0
for i in range (3,len(a)-1):
    if a[i-2]<a[i-1] and a[i-1]>a[i]:
        c+=1
print(c)

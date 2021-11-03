a=[1, 2, 4, 7, 9, 7, 6, 0, 7, 3, 5, 7, 7, 8]
a.sort()
print(a)
c=0
for i in range(2, len(a)): 
    if a[i-2]==a[i-1] or a[i-1]==a[i]:
        c+=1
print(len(a)-c)

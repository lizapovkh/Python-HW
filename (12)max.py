a=[1, 2, 4, 7, 9, 7, 6, 0, 7, 3, 5, 7, 7, 8, 9, 9]
a.sort()
print(a)
max=0
j=len(a)
for i in range(j): 
    if a[i]==a[j-1]:
        max=a[i]
        break
    else:
        max=a[j-1]
print(max)
print(i)

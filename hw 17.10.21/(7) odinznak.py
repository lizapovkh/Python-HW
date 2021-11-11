a=[1, 5, 7, -9, 8, -2, -3, 6]
for i in range(1,len(a)):
    if (a[i-1]>0 and a[i]>0) or (a[i-1]<0 and a[i]<0):
        print(a[i-1])
        print(a[i])
        break

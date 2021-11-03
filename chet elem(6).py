a=[1, 3, 102, 64, 87, 94, 71]
b=[]
for i in range (len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(b)

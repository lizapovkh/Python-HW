a=[1, 2, 3, 4, 5, 6, 7]
b=[7, 6, 5, 4, 3, 2, 1]
c=[]
x=0
for i in range (len(a)):
    x=a[i]+b[i]
    c.append(x)
print(c)

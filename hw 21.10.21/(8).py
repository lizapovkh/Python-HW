a=[int(s) for s in input().split()]
a.append(0)
k=int(input())
c=int(input())
for i in range(len(a)-1,k,-1):
    a[i]=a[i-1]
a[k]=c
print(a)

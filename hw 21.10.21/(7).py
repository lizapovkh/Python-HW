a=[int(s) for s in input().split()]
k=int(input())
for i in range(k+1, len(a)):
    a[i-1]=a[i]
a.pop()
print(a)

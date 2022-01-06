a= {}
for i in input().split():
    a[i]=a.get(i,0)+1
    print(i,'-', int(a[i]-1), end=';')

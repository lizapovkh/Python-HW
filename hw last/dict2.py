n= int(input())
a={}
for i in range (n):
    s1, s2 = input().split('-')
    a[s1]= s2
    a[s2]= s1
print(a[input()])

a=[1, 2, 3, 4, 5, 6]
n=len(a)
def sredn():
    c=0
    for i in range (n):
        c+=a[i]
    s=c/n
    return s
print(sredn())
        

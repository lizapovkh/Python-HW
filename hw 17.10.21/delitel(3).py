n=int(input())
a=0
for i in range (2,n+1):
    if n%i==0:
        a=i
        break
if n<2:
    print('error')
else:
    print(a)
            
        
        

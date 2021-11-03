n=int(input())
f_0=0
f_1=1
for i in range(2,n+1):
    f_n= f_1+f_0
    f_0=f_1       
    f_1=f_n
print('f_%s: %s' %(n, f_n))

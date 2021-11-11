def is_prime(a):
    b=0
    flag=False
    for i in range(1,a+1):
        if a%i==0:
            b+=1
    if b==2:
        flag=True
    return flag
a=int(input())
print(is_prime(a))
        

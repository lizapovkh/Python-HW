a=int(input('a='))
b= int(input('b='))
if a>b:
    c= a-b
    a=b
    b=a+c
else:
    c=b-a
    b=a
    a=b+c
print('a=',a)
print('b=',b)

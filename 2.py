#1 способ
a= input()
b= input()
c=input()
n=a+b+c
m=int(a)* int (b) * int (c)
print (n)
print (m)

#2 способ (лучше)

a= int(input())
b= int(input())
c= int(input())
n= 100*a+10*b+c
m= a*b*c
if (a<10) and (b<10) and(c<10):
    print(n,'   ',m)
else:
    print(False)

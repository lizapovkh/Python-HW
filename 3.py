#1 способ
a= input()
b= input()
c=input()
n=a+b+c

x=input()
y= input()
z=input()
q=x+y+z


print (n)
print (q)
print(n+q)

#2 способ (лучше)
a= int(input())
b= int(input())
c= int(input())
n= 100*a+10*b+c
x= int(input())
y= int(input())
z= int(input())
m= 100*x+10*y+z
l=(str(n)+str(m))
if (a<10) and (b<10) and (с<10) and (x<10) and (y<10) and (z<10):
    print(n,'   ',m)
    print(l)
else:
    print(False)

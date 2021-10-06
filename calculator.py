#Выполняет сразу все операции

x=int(input('введите первое число\n')) 
y=int(input('введите второе число\n'))
c=x+y
d=x-y
h=x*y
m=x/y
print('сумма = ', c)
print('разность = ',d)
print('произведение = ', h)
print('частное = ', m)

#Выполняет только заданную операцию

x=float(input()) #1 число
z=str(input()) #операция
y=float(input()) #2 число
c=x+y
d=x-y
h=x*y
m=x/y
if z=='+':
    if c%1==0:
        print(int(c))
    else:
        print(c)
if z=='-':
    if d%1==0:
        print(int(d))
    else:
        print(d)
if z=='*':
    if h%1==0:
        print(int(h))
    else:
        print(h)
if z=='/':
    if m%1==0:
        print(int(m))
    else:
        print(m)



print('чтобы перевести число в двоичную систему- введите  код "2", в десятичную - "10" ')
d=int(input('код: '))
if d==2:
    def two():
        x=int(input('введите десятичное число: '))
        c=[]
        b=0
        while x!=1:
            b=x%2
            c.append(str(b))
            x//=2
        c.append('1')
        c.reverse()
        a=''
        for j in range(len(c)):
            a+=c[j]
        return a
    print(two())
elif d==10:
    def ten():
        y=int(input('введите двоичное число: '))
        m=0
        w=0
        while y>0:
           m+=y%10*2**w
           w+=1
           y//=10
        return m
    print(ten())




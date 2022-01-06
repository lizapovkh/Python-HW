a=[int(b) for b in input ().split()]
c= set()
for i in a:
    if i in c:
        print('yes')
    else:
        print('no')
        c.add(i)

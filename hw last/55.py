a= set()
print('введите количество слов:')
b=int(input())
print('введите %s слов' %(b))
for i in range (b):
    a.update (input().split())
print(len(a))

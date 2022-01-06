world = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        world[city] = country
         
for i in range(int(input())):
    print(world[input()])

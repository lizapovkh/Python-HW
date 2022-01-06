c = {}
for i in range(int(input())):
    line = input().split()
    for j in line:
        c[j] = c.get(j, 0) + 1
max_count = max(c.values())
most_frequent = [k for k, v in c.items() if v == max_count]
print(min(most_frequent))

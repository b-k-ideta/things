total = 0
for i in range(1000):
    if i%5 == 0:
        total += i
        print(i)
    elif i%3 == 0:
        total += i
        print(i)

print(total)
y = int(input("縦"))
x = int(input("横"))
cnt = 0
for i in range(y):
    for j in range(x):
        if cnt%2 == 0:
            print("#", end="")
        else:
            print(".", end="")
        cnt +=1
    cnt +=1
    print()
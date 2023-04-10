for i in range(6):
    if i%2 == 0:
        block = "■"
    else:
        block = "□"
    for j in range(10):
        print(block, end="")
    print()

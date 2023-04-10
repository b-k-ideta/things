multiplys = []

# for i in range(9):
#     temp = []
#     for j in range(9):
#         temp.append((i+1)*(j+1))
#     multiplys.append(temp)

# for i in range(9):
#     for j in range(9):
#         print(multiplys[i][j], " ", end="")
#     print()

for i in range(9):
    for j in range(9):
        print(f"{(i+1)*(j+1)}", " ", end="")
    print()
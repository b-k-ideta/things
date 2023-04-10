colors = ["blue", "red", "yellow", "red", "greens","red", "red"]
print("削除前:", colors)
target = "red"


"""
while target in colors :
  colors.remove(target)
print("削除後:", colors)
""" 
# for i in colors:
#     print(i)
#     if i != target:
#         continue
#     else:
#         colors.remove(target)

colors2 = []
for i in colors:
    # print(i)
    if i != target:
        colors2.append(i)
colors = colors2
print("削除後:", colors)

# colors = [i for i in colors if i != target]
# print(colors)

# for i in range(len(colors)):
#     print(i)
#     if colors[i] == target:
#         colors.pop(i)
# print("削除後:", colors)
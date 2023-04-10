# ホワイトボード問題
# 1
nums = [1,2,3,4,5,6]
nums_double = [(i*2) for i in nums]
print(nums_double)
# 2
multi5_list = []

for i in range(101):
    if i%5 == 0:
        multi5_list.append(i)

print(multi5_list)
# 3
result = [i for i in range(101) if i%5==0]
print(result)
# 4
nums = [1,2,3,4,5]
names = []
for i in nums:
    in1 = input("名前を入力してください: ")
    names.append(in1)
names2 = dict(zip(nums, names))
print(names2)
print(names2[2])

nums = []
total = 0
# count = 0

while 1:
    in1=int(input("数値を入力してください: "))
    if in1==0:
        break
    else:
        nums.append(in1)
        # count += 1

for i in nums:
    total += i

median = int(len(nums)/2)
print(median)
if len(nums)%2 == 0:
    median = (nums[median]+nums[median-1])/2
else:
    median = nums[median]

print(f"入力値: {nums}")
print(f"中央値は{median}です。")
print(f"平均は{total/len(nums)}です。")


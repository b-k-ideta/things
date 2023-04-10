nums = []
total = 0

while 1:
    try:
        in1 = int(input("数値を入力してください: "))
        if in1 == 0:
            break
        nums.append(in1)
    except ValueError:
        print("正しい値を入力してください")
    

for i in nums:
    total += i

try:
    median = int(len(nums)/2)
    if len(nums)%2 == 0:
        median = (nums[median]+nums[median-1])/2
    else:
        median = nums[median]
    print(f"合計は{total}です。")
    print(f"中央値は{median}です。")
    print(f"平均は{total/len(nums)}です。")
except Exception:
    print("数値が入力されませんでした。")
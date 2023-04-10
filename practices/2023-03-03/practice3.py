nums = []

while 1:
    try:
        num = input("数字の入力をしてね。")
        if num == "end":
            break
        else: 
            nums.append(int(num))
    except Exception as err:
        print(err)

print(nums)
# print(f"合計は{total}です。")
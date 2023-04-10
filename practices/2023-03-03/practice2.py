total = 0

while 1:
    try:
        num = int(input("数字の入力をしてね。"))
        if num == 0:
            break
        else: 
            total += num
    except Exception as err:
        print(err)

print(f"合計は{total}です。")

total2 = 0

for i in range(100):
    if (i+1)%2 ==0:
        total2 += (i+1)

print(f"1から100までの偶数の総和は{total2}です。")

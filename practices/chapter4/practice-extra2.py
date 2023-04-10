total=0

print("入力された二つの数値から総和を求めます。")

while 1:    
    try:
        m = int(input("一つ目の数値を入力: "))
        n = int(input("二つ目の数値を入力: "))
        if m > n:
            temp = n
            n = m
            m = temp
        break
    except ValueError:
        print("正しい数値を入力してください。")

# for i in range(m, n+1):
#     total+= i
i = m
while i <= n:
    total += i
    i += 1

print(f"{m}から{n}までの総和は{total}です。")

total = 0
flag = True

while flag == True:
    in1 = int(input("数値を入力してください: "))
    if in1 == 0:
        flag = False
    total += in1
 
print("合計は", total, "です。")
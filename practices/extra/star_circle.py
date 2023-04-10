disp = ""


while 1:
    try:
        # 表示回数をcicleに代入
        cicle = int(input("表示する回数を入力: "))
        for i in range(cicle):
            # iが偶数時に○、奇数時に★
            if i%2 == 0:
                disp += "○"
            else:
                disp += "★"
            # 最後のループ以外はカンマをつける
            if i != cicle-1:
                disp += ","
        break
    except ValueError:
        print("正しい数値を入力してください。")
    
print(disp)
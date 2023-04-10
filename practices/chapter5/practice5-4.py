from random import randint as dice
error_def = "無効な値です。"

while 1:
    try:
        dice_dx = int(input("目の数を数値を入力してください。>>>"))
        if dice_dx<1:
            print("0より大きい値を指定してください。")
            continue
        break
    except ValueError:
        print(error_def)

while 1:
    try:
        choice = int(input("1:サイコロを振る\t2:終了 >>>"))
        if choice == 1:
            print(f"D{dice_dx}  サイコロの目は{dice(1, dice_dx)}です。")
        elif choice == 2:
            break
        else:
            print(error_def)
    except ValueError:
        print(error_def)

print("終了します。")
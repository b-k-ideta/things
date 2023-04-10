user_in:str = ""
total = 0
cnt = 0
while "End" != user_in:
    try:
        user_in = input("入力してください")
        if user_in == "End":
            pass
        else:
            total += int(user_in)
            cnt += 1
    except Exception as err:
        print(err)
    
print(cnt,"回入力しました")
print(f"合計は{total}です。")
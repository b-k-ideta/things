while 1:
    try:
        score = int(input("テストの点数を入力してください: "))
        if score >= 80:
            print("合格")
        else:
            print("不合格")
        break
    except Exception as error:
        print("正しい値を入力してください。")
        print(error)
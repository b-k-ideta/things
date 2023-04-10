print("今は朝:0・昼:1・夜:2のどれですか？")
in1 = input("該当する数字を入力してください")

if int(in1) == 0:
    print("おはようございます。")
elif int(in1) == 1:
    print("こんにちは。")
elif  int(in1) == 2:
    print("こんばんは。")
else:
    print("入力エラー")


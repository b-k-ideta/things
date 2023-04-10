
# テストの点数を入力
t1 = int(input("国語の点数: "))
t2 = int(input("算数の点数: "))
t3 = int(input("英語の点数: "))

# テストの平均を求める
ta = (t1+t2+t3)/3

# 全教科80点以上は「優」、平均点70点以上は「良」、全教科60点以上は可、それ以外は「不」
if t1>=80 and t2>=80 and t3>=80:
    print("優")
elif ta >= 70:
    print("良")
elif t1>=60 and t2>=60 and t3>=60:
    print("可")
else:
    print("不")
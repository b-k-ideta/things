# def sum(num1, num2):
#     return num1+num2


# def sub(num1, num2):
#     return num1-num2


# def mul(num1, num2):
#     return num1*num2


# def div(num1, num2):
#     return num1/num2

def calc():
    while 1:
        try:
            num1 = int(input("数字入力1:"))
            num2 = int(input("数字入力2:"))
            operator = input("演算子入力")
            if operator == "+" or operator == "-" or \
            operator == "*" or operator == "/":
                result = eval(f"{num1} {operator} {num2}")
            else:
                print("演算子の入力がされてません。")
                continue
            print(f"{num1} {operator} {num2} = {result}")
            break
            # if operator == "+":
            #     result = sum(num1, num2)
            # elif operator == "-":
            #     result = sub(num1, num2)
            # elif operator == "*":
            #     result = mul(num1, num2)
            # elif operator == "/":
            #     if num2 == 0:
            #         print("0で割れません。")
            #         continue
            #     result = div(num1, num2)
            # else:
            #     print("演算子の入力がされてません。")
            #     continue
            # print(f"{num1} {operator} {num2} = {result}")
            # break
        except Exception as err:
            print(err)

decision = 0

while decision == 0:
    calc()
    try:
        decision = int(input("計算を続けますか？[0]続ける\t[1]やめる>>>"))
        if decision == 0:
            pass
        elif decision == 1:
            break
        else:
            print("0か1を入力してください。")
    except Exception as err:
        print(err)

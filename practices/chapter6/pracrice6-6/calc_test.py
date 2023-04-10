import calc

# 入力関数
def user_input(what_num=0):
    while 1:
        try:
            user_in = int(input(f"{what_num}つ目の値 >>>"))
            return user_in
        except Exception:
            print("無効な値です。")


def main():
    first = user_input(1)
    second = user_input(2)

    calc.add(first, second)
    calc.sub(first, second)
    calc.mul(first, second)
    calc.div(first, second)


if __name__ == "__main__":
    main()

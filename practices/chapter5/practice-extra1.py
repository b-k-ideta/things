from random import randint, choice
error_def = "無効な値です。"

omikuji = ("大凶","凶","末吉","小吉","吉","中吉","大吉")
# o_dict = {1:"大凶",2:"凶",3:"末吉",4:"小吉",5:"吉",6:"中吉",7:"大吉"}

while 1:
    try:
        c = int(input("1:おみくじを引く\t2:終了 >>>"))
        match c:
            case 1:
                print(f"{omikuji[randint(0,len(omikuji)-1)]}です。")
                # disp = choice(list(o_dict.values()))
                # print(f"{disp}です。")
            case 2:
                break
            case _:
                raise ValueError
    except ValueError:
        print(error_def)

print("終了します。")
import random


def main():
    main_loop()

def main_loop():

    rps = {0:"Rock", 1:"Paper", 2:"Scisor"}

    # 勝ち負け判定用関数
    def judge(user, com):
        result = (user-com+3)%3
        match result:
            case 0:
                print(f"{rps[user]}\t{rps[com]}")
                print("Draw")
            case 1:
                print(f"{rps[user]}\t{rps[com]}")
                print("You Win!")
            case 2:
                print(f"{rps[user]}\t{rps[com]}")
                print("You Lose!")
        

    #メインループ
    while 1:
        #プレイヤー入力
        while 1:
            try:
                user_in = int(input("Rock[0],Paper[1] or Scirsor[2]? >>>"))
                if user_in < 0 or user_in > 2:
                    raise Exception
                break
            except Exception:
                print("ERROR")
        
        com_in = random.randint(0,2)
        
        judge(user_in, com_in)




if __name__ == "__main__":
    main()
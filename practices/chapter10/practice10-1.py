import random
import os

def_error = "無効な入力です。"

# プレイヤーとコンピューターのクラス
class Player:

    # ●×を格納していくリスト
    __player_wincnt = []

    def __init__(self, decision=0):
        self.__decision = decision

    @property
    def decision(self):
        return self.__decision

    def player_wincnt():
        return Player.__player_wincnt

    # 勝敗カウント
    def add_player_wincnt(res):
        if res == 1:
            Player.__player_wincnt.append("×")
            return
        elif res == 2:
            Player.__player_wincnt.append("○")
            return
        else:
            return

    # プレイヤーの選択用メソッド
    def pl_decision(self):
        while 1:
            try:
                pl_input = int(input("1:グー,2:チョキ,3:パー>>>"))
            except Exception as err:
                print(err)
            if pl_input < 4 and pl_input > 0:
                self.__decision = int(pl_input)
                return
            else:
                print(def_error)

    # コンピューターの選択用メソッド
    def com_decision(self):
        self.__decision = random.randint(1, 3)
        return self.__decision

    # 勝敗の判断用の値を返すメソッド
    def judge_result(dec1, dec2):
        result = ((dec1-dec2)+3) % 3
        return result

# ゲームループ
class Game:

    dict_rps = {1: "グー", 2: "チョキ", 3: "パー"}

    def main_loop(pl: Player, com: Player):
        while 1:
            os.system("cls")
            print("じゃんけん・・・")
            flag = 0
            # あいこ用ループ
            while flag == 0:
                # プレイヤーとCOMの手の選択
                pl.pl_decision()
                com.com_decision()
                # 手の表示
                Game.display_both(pl.decision, com.decision)
                # 結果判断
                result = Player.judge_result(pl.decision, com.decision)
                # ループを抜ける判断
                flag = Game.win_or_lose(result)
            # 勝敗カウントを表示
            Game.win_count_disp(Player.player_wincnt())
            while 1:
                continue_or_not = input("続けますか？(y/n)>>>")
                if str.lower(continue_or_not) == "n":
                    quit()
                elif str.lower(continue_or_not) == "y":
                    break
                else:
                    print(def_error)

    # 選択した手を表示するメソッド
    def display_both(pl, com):
        print("あなたの手", Game.dict_rps[pl])
        print("コンピューターの手", Game.dict_rps[com])

    # 勝ち負けの判断とあいこループ解除用メソッド
    def win_or_lose(res):
        match res:
            case 0:
                # os.system("cls")
                print("あいこで・・・")
                return 0
            case 1:
                # 勝敗カウントに追加
                Player.add_player_wincnt(res)
                print("あなたの負けです。")
                return 1

            case 2:
                # 勝敗カウントに追加
                Player.add_player_wincnt(res)
                print("あなたの勝ちです。")
                return 2

    # 成績表示メソッド
    def win_count_disp(lst):
        pl_win = 0
        print("===成績============================")
        print("YOU: ", end="")
        for i in lst:
            print(i, end="")
        print()
        print("COM: ", end="")
        for i in lst:
            if i == "○":
                print("×", end="")
            else:
                print("○", end="")
        print()
        for i in lst:
            if i == "○":
                pl_win += 1
        print(f"{pl_win}勝 {len(lst)-pl_win}負")
        print("=================================")


def main():
    player_obj = Player()
    com_obj = Player()

    Game.main_loop(player_obj, com_obj)


if __name__ == "__main__":
    main()

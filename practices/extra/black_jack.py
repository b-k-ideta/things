import random
import os
import time

default_error = "無効な数値です。正しい値を入力してください。"

# タイトルメニュー
def main():

    while 1:
        os.system('cls')
        print("BBBBB    LL          AAA       CCCCCC  KK  KKK ")
        print("BB   BB  LL         AA AA     CCC      KK KKK  ")
        print("BBBBB    LL        AA   AA    CC       KKKK    ")
        print("BB   BB  LL       AAAAAAAAA   CCC      KK KKK   ")
        print("BBBBB    LLLLLL  AAA     AAA   CCCCCC  KK  KKK \n")
        
        print("             JJ      AAA       CCCCCC  KK  KKK ")
        print("             JJ     AA AA     CCC      KK KKK  ")
        print("             JJ    AA   AA    CC       KKKK    ")
        print("         JJ  JJ   AAAAAAAAA   CCC      KK KKK   ")
        print("         JJJJJ   AAA     AAA   CCCCCC  KK  KKK \n")

        try:
            start_game = int(input("\n[0]START GAME  [1]QUIT GAME \n"))
            if start_game == 0:
                game_loop()
            elif start_game == 1:
                quit()
            else:
                print(default_error)
                time.sleep(1)
                continue
        except ValueError:
            print(default_error)
            time.sleep(1)
            continue

# ゲームループ
def game_loop():
    # インスタンス用
    suits_types = ["♠", "♥", "♣", "♦"]
    numbers_id = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "K", "Q", "J"]
    # 判定用
    numbers = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
               "7": 7, "8": 8, "9": 9, "10": 10, "K": 10, "Q": 10, "J": 10}
    # 勝敗（勝ち、負け、引き分け）
    win_cnt = [0,0,0]
    # 誰が勝ったかフラグ（初期値は0＝誰でもない）
    winner = 0

    # カードのクラス

    class Trump():
        def __init__(self, suits, number):
            self.suits = suits
            self.number = number

    # デッキ構築用関数

    def deck_creator(deck):
        for i in range(len(suits_types)):
            for j in range(len(numbers_id)):
                deck.append(Trump(suits_types[i], numbers_id[j]))

    # デバッグ用関数

    def deck_verifier(deck):
        for i in range(len(deck)):
            print(f"Card{i}:", deck[i].suits, deck[i].number)

    # カードを配布

    def dealer(deck):
        return deck.pop()

    # バスト判定

    def bust(total):
        if total > 21:
            return True
        else:
            return False


    # 表示用関数（コメントアウト部はデバッグ用）
    def pl_com_disp():
        os.system('cls')
        print(f"プレイヤー:{win_cnt[0]}勝    COM:{win_cnt[1]}勝    引き分け:{win_cnt[2]}\n")
        print("プレイヤー")
        for i in range(len(player_cards)):
            print(
                f"手札{i+1}: {player_cards[i].suits}{player_cards[i].number}")
        print("\nCOM")
        if result == True:
            for i in range(len(com_cards)):
                print(f"手札{i+1}: {com_cards[i].suits}{com_cards[i].number}")
        else:
            print(f"表カード: {com_cards[0].suits}{com_cards[0].number}")
            for i in range(len(com_cards)-1):
                print("伏せカード")

    # エース判定用兼合計計算呼び出し関数

    def calc_aces(cards, total):
        
        # 合計の一時的な集計
        def total_calc(cards, total_tmp):
            total_tmp = 0
            for i in cards:
                temp = numbers[i.number]
                total_tmp += temp
            return total_tmp

        # エース持ち２１以上にならないように計算
        def ace_calc(total_recalc, aces_cnt):
            if total_recalc <= 21:
                return total_recalc
            else:
                if aces_cnt > 0:
                    total_recalc = total_recalc - 10
                    aces_cnt -= 1
                    return ace_calc(total_recalc, aces_cnt)
                else:
                    return total_recalc
                
        aces = 0
        total = total_calc(cards, total)

        for i in cards:
            if i.number == "A":
                aces += 1
        if aces > 0:
            total += 10*aces
            total = ace_calc(total, aces)
        return total

    # 勝敗判定

    def when_stand(pl_total, com_total):
        if pl_total > com_total and pl_total < 22:
            return 1
        elif com_total > pl_total and com_total < 22:
            return 2
        else:
            return 3
        

    # 勝敗メッセージ

    def post_msg(winner):
        if winner == 1:
            print("\nYou win!\n")
            print(pl_total, com_total)
        elif winner == 2:
            print("\nYou lose!\n")
            print(pl_total, com_total)
        elif winner == 3:
            print("\nDraw!\n")
            print(pl_total, com_total)


    # 勝敗点数加算
    def cnt_func(winner, win_cnt):
        match winner:
            case 0:
                return win_cnt
            case 1:
                win_cnt[0] += 1
                return win_cnt
            case 2:
                win_cnt[1] += 1
                return win_cnt
            case 3:
                win_cnt[2] += 1
                return win_cnt




    # ゲーム終了関数

    def game_over(flag):
        while flag == False:
            try:
                continue_or_not = int(input("\nゲームを続けますか？ [0]はい [1]いいえ\n"))
                if continue_or_not > 1:
                    print(default_error)
                    time.sleep(1)
                    continue
                elif continue_or_not == 0:
                    flag = True
                else:
                    quit()
            except ValueError:
                print(default_error)
                time.sleep(1)
                continue
        return flag

    while 1:
        # 初期化等
        deck = []
        player_cards = []
        com_cards = []
        # 合計用
        pl_total = 0
        com_total = 0
        deck_creator(deck)
        random.shuffle(deck)
        # 初回ターンフラグ
        first_turn = True
        # ゲームオーバーフラグ
        game_over_f = False
        # COM手札表示用フラグ
        result = False
        # 勝敗カウント
        win_cnt = cnt_func(winner, win_cnt)
        # 勝者初期化
        winner = 0
        
        # メインループ
        while game_over_f == False:

            if first_turn == True:
                os.system('cls')
                print(f"プレイヤー:{win_cnt[0]}勝    COM:{win_cnt[1]}勝    引き分け:{win_cnt[2]}\n")
                # プレイヤー初回カード配布
                print("プレイヤー")
                for i in range(2):
                    player_cards.append(dealer(deck))
                    print(f"手札{i+1}: {player_cards[i].suits}{player_cards[i].number}")
                    time.sleep(0.3)
                # ディーラー初回カード配布
                for i in range(2):
                    com_cards.append(dealer(deck))
                print("\nCOM")
                print(f"表カード: {com_cards[0].suits}{com_cards[0].number}")
                time.sleep(0.3)
                print("伏せカード")
                time.sleep(1.8)

                # スプリット可能かどうか
                if player_cards[0].number == player_cards[1].number:
                    while 1:
                        pl_com_disp()
                        try:
                            split_yn = int(input("スプリットしますか？ [0]はい [1]いいえ\n"))
                            if split_yn == 0:
                                player_cards.pop()
                                player_cards.append(dealer(deck))
                                pl_com_disp()
                                break
                            elif split_yn == 1:
                                break
                            else:
                                print(default_error)
                                time.sleep(1)
                                continue
                        except ValueError:
                            print(default_error)
                            time.sleep(1)
                            continue

                pl_total = calc_aces(player_cards, pl_total)
                com_total = calc_aces(com_cards, com_total)
                # ブラックジャック引き分け
                if (pl_total == 21) == True and (com_total == 21) == True:
                    result = True
                    pl_com_disp()
                    print("\nBLACK JACK")
                    time.sleep(0.3)
                    winner = 3
                    win_cnt = cnt_func(winner, win_cnt)
                    post_msg(winner)
                    game_over_f = game_over(game_over_f)
                # プレイヤーブラックジャック勝ち
                elif (pl_total == 21) == True:
                    result = True
                    pl_com_disp()
                    print("\nBLACK JACK")
                    time.sleep(0.3)
                    winner = 1
                    post_msg(winner)
                    game_over_f = game_over(game_over_f)
                # COMブラックジャック勝ち
                elif (com_total == 21) == True:
                    result = True
                    pl_com_disp()
                    print("\nBLACK JACK")
                    time.sleep(0.3)
                    winner = 2
                    post_msg(winner)
                    game_over_f = game_over(game_over_f)
                # 初回ターンフラグOFF
                first_turn = False

            else:
                pl_com_disp()

                pl_total = calc_aces(player_cards, pl_total)
                com_total = calc_aces(com_cards, com_total)

                # プレイヤーにヒット（カードを引く）かスタンド（手持ちで勝負）の選択
                try:
                    player_input = int(input("\nヒット[0]（カードを引く）　スタンド[1]（手持ちで勝負）\n"))
                    # カードを引く
                    if player_input == 0:
                        player_cards.append(dealer(deck))
                        pl_total = calc_aces(player_cards, pl_total)
                        if bust(pl_total) == True:
                            result = True
                            pl_com_disp()
                            winner = 2
                            post_msg(winner)
                            game_over_f = game_over(game_over_f)
                        else:
                            pass
                    # 手持ちで勝負
                    elif player_input == 1:
                        # COMが引くかどうかの判定
                        while com_total < 17:
                            com_cards.append(dealer(deck))
                            com_total = calc_aces(com_cards, com_total)
                            if bust(com_total) == True:
                                result = True
                                pl_com_disp()
                                winner = 1
                                post_msg(winner)
                                game_over_f = game_over(game_over_f)
                            else:
                                pl_com_disp()
                        result = True
                        pl_total = calc_aces(player_cards, pl_total)
                        com_total = calc_aces(com_cards, com_total)
                        winner = when_stand(pl_total, com_total)
                        pl_com_disp()
                        post_msg(winner)
                        game_over_f = game_over(game_over_f)
                    else:
                        print(default_error)
                        time.sleep(1)
                        continue
                except ValueError:
                    print(default_error)
                    time.sleep(1)
                    continue

                # COMが引くかどうかの判定
                if com_total < 17:
                    com_cards.append(dealer(deck))
                    com_total = calc_aces(com_cards, com_total)
                    if bust(com_total) == True:
                        result = True
                        pl_com_disp()
                        winner = 1
                        post_msg(winner)
                        game_over_f = game_over(game_over_f)
                else:
                    pl_com_disp()

if __name__ == "__main__":
    main()

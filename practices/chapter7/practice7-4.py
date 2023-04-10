import csv
default_error = "エラーです。"
cancel_msg = "キャンセルします。"


# メニュー
def menu():
    while 1:
        try:
            user_in = int(input("1:表示　2:登録　3:削除　9:終了　>>>"))
            match user_in:
                case 1:
                    c_reader()
                case 2:
                    c_register()
                case 3:
                    c_remove()
                case 9:
                    print("終了します。")
                    quit()
                case _:
                    print(default_error)
        except Exception as err:
            print(err)
            print(default_error)


# 表示 as err
def c_reader():
    c_data = read_csv()

    # # CSVの書式から二次元配列へ
    # c_disp = []
    # for i in c_data:
    #     temp = i.split(",")
    #     temp[0] = int(temp[0])
    #     temp[1] = temp[1].strip('"')
    #     temp[2] = temp[2].strip('"')
    #     temp[2] = temp[2].strip('"\n')
    #     c_disp.append(temp)

    # 一行ずつ表示
    # for i in c_disp:
    for i in c_data:
        print(f"ID:{i[0]}　会社名:{i[1]}　会社住所:{i[2]}")

    return


# ID検索
def id_searcher(id_in, array):
    for i in array:
        if int(i[0]) == id_in:
            data = i
            return True, data
    data = i
    return False, data

# CSV読み込み
def read_csv():
    with open("test\\chapter7\\company.csv", "r", encoding="utf-8") as f:
        # array = f.readlines()
        reader = csv.reader(f)
        array = [row for row in reader]
    return array

# CSV書き込み
def write_csv(array):
    with open("test\\chapter7\\company.csv", "w", encoding="utf-8", newline="") as f:
        # f.writelines(array)
        writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(array)
        f.flush()
    return

# 無駄が多いソート処理
def csv_sort(array):
    tmp_array =[]
    for i in array:
        i[0] = int(i[0])
        tmp_array.append(i)
    # for i in array:
    #     temp = i.split(",")
    #     temp[0] = int(temp[0])
    #     temp[1] = temp[1].strip('"')
    #     temp[2] = temp[2].strip('"')
    #     temp[2] = temp[2].strip('"\n')
    #     tmp_array.append(temp)
    tmp_array.sort()

    # tmp_array2 =[]
    # for d in tmp_array:
    #     s= str(d[0])+","
    #     s +='"'+d[1]+'"'+","
    #     s +='"'+d[2]+'"'+"\n"
    #     tmp_array2.append(s)
    
    # return tmp_array2
    return tmp_array


# 登録
def c_register():

    c_data = read_csv()

    while 1:
        try:
            c_id = int(input("IDを入力してください　>>>"))
            if c_id < 1:
                print(cancel_msg)
                return
            flag, _= id_searcher(c_id, c_data)
            if flag == True:
                print("そのIDはすでに登録済みです。")
                continue
            c_name = input("会社名を入力してください　>>>")
            c_address = input("会社の住所を入力してください　>>>")
            break
        except Exception as err:
            print(err)
            print(default_error)
            

    # CSVの書式にする
    # s = str(c_id)+","
    # s += '"'+c_name+'"'+","
    # s += '"'+c_address+'"'+"\n"
    tmp_data = [c_id, c_name, c_address]
    c_data.append(tmp_data)
    # c_data.sort()
    c_data = csv_sort(c_data)
    print("登録しました。")

    write_csv(c_data)
 
    return


# 削除
def c_remove():

    c_data = read_csv()

    while 1:
        try:
            c_id = int(input("削除したいIDを入力してください　>>>"))
            if c_id < 1:
                print(cancel_msg)
                return
            flag, tmp_element = id_searcher(c_id, c_data)
            if flag == False:
                print("そのIDは未登録です。")
                continue
            break
        except ValueError:
            print(default_error)

    c_data.remove(tmp_element)

    print("データを削除しました。")
    
    write_csv(c_data)
    
    return


def main():
    menu()


if __name__ == "__main__":
    main()

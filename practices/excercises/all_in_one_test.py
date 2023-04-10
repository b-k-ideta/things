import mysql.connector as mydb

def menu(cursor,connect):
    while 1:
        connect.ping(reconnect=True)
        print("-------------メニュー画面----------------")
        try:
            user_input= int(input("1:テーブル情報取得\t2:データ挿入\
                                \n3:データ更新\t4:データ削除\t9:終了\n>>>"))
            match int(user_input):
                case 1:
                    search(cursor)
                case 2:
                    insert_d(cursor, connect)
                case 3:
                    update_d(cursor,connect)
                case 4:
                    delete_d(cursor,connect)
                case 9:
                    return
                case _:
                    continue
        except Exception as err:
            print(err)
            continue

def search(cursor):
    while 1:
        try:
            print("-------------情報取得----------------")
            user_input= int(input("1:テーブル取得\t2:データ検索\t9:終了\n>>>"))
            match int(user_input):
                case 1:
                    cursor.execute("select * from author")
                case 2:
                    serach_input = input("検索したい名前の入力(空白でキャンセル): ")
                    if serach_input == "":
                        continue
                    serach_input = "%"+serach_input+"%",
                    cursor.execute("select * from author\
                        where name like %s", serach_input)
                case 9:
                    return
        except Exception as err:
            print(err)
            continue

        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print(cursor.rowcount, "件、取得しました")
        

def insert_d(cursor, connect):
    while 1:
        try:
            print("-------------データ挿入----------------")
            id= input("IDを入力: ")
            name_kan = input("名前を入力: ")
            name_kana = input("名前の仮名を入力: ")
            data = (id, name_kan, name_kana)
            confirm = input(data,"以上を挿入します。よろしいですか？(y/n)")
            if confirm == "y":
                pass
            elif confirm =="n":
                return
            else:
                print("無効な入力です。")
                continue
            cursor.execute("insert into author values(%s,%s,%s)", data)
            print(cursor.rowcount,"件、挿入しました。")
            connect.commit()
            return
        except Exception as err:
            print(err)
            continue


def update_d(cursor, connect):
    while 1:
        try:
            print("-------------データ更新----------------")
            id= input("名前を変更したいIDを入力: "),
            cursor.execute("select * from author\
                        where author_id = %s", id)
            row = cursor.fetchone()
            if 0 == cursor.rowcount:
                print("未登録です。")
                return
            name_kan = input("更新後の名前を入力: ")
            name_kana = input("更新後の名前の仮名を入力: ")
            data = (name_kan, name_kana, id[0])
            confirm = input(f"{row}->({id[0],name_kan,name_kana})に変更します。\
                                      よろしいですか？(y/n)")
            if confirm == "y":
                pass
            elif confirm =="n":
                return
            else:
                print("無効な入力です。")
                continue
            cursor.execute("update author set name=%s, name_kana=%s where author_id =%s", data)
            print(cursor.rowcount,"件、更新しました。")
            connect.commit()
            return
        except Exception as err:
            print(err)
            continue


def delete_d(cursor, connect):
    while 1:
        try:
            print("-------------データ削除----------------")
            id= input("削除したいIDを入力: "),
            cursor.execute("select * from author\
                        where author_id = %s", id)
            row = cursor.fetchone()
            if 0 == cursor.rowcount:
                print("未登録です。")
                return
            confirm = str.lower(input(f"{row}を削除します。よろしいですか？(y/n)"))
            if confirm == "y":
                pass
            elif confirm =="n":
                return
            else:
                print("無効な入力です。")
                continue
            cursor.execute("delete from author where author_id=%s", id)
            print(cursor.rowcount,"件、削除しました。")
            connect.commit()
            return
        except Exception as err:
            print(err)
            continue


def main():

    # コネクションの作成
    conn = mydb.connect(
        host ="localhost",
        port ="3306",
        user ="user",
        password="pass",
        database="book"
    )
        
    # カーソルの作成
    cur = conn.cursor()

    # 入力ループ
    menu(cur, conn)
    

    # # SQL文の実行
    # # cur.execute(f"select * from author\
    # #             where author_id like '{user_input}' ")
    # cur.execute(query)
    
    # # 実行結果を取得
    # rows = cur.fetchall()

    # for row in rows:
    #     print(row)

    # カーソルの切断
    cur.close()

    # コネクションの切断
    conn.close()

if __name__ == "__main__":
    main()
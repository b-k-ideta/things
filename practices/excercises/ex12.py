import mysql.connector as mydb
import matplotlib.pyplot as plt

def main():
    # コネクションの作成
    conn = mydb.connect(
        host ="localhost",
        port ="3306",
        user ="user",
        password="pass",
        database="ex"
    )
        
    # カーソルの作成
    cur = conn.cursor()

    
    

    # # SQL文の実行
    cur.execute(f"select * from test_average")
    # cur.execute(query)
    
    rows = cur.fetchall()


    plt.rcParams["font.family"] = "MS Gothic"
    a_x, a_y = range(0, 5), rows[0][2:]
    b_x, b_y = range(0, 5), rows[1][2:]
    labels = ["japanese", "math", "science", "socialstudies", "english"]
    
    fig = plt.figure()    # 図を作る
    
    # 1行2列の左
    ax1 = fig.add_subplot(1, 2, 1)    # サブプロットを追加する
    ax1.bar(a_x, a_y, color = "b", tick_label = labels)    # グラフの描画
    ax1.set_title("A組")    # グラフのタイトル
    ax1.set_yticks([0,20,40,60,80,100])
    # 1行2列の右
    ax2 = fig.add_subplot(1, 2, 2)    # サブプロットを追加する
    ax2.bar(b_x, b_y, color = "g", tick_label = labels)    # グラフの描画
    ax2.set_title("B組")    # グラフのタイトル
    ax2.set_yticks([0,20,40,60,80,100])
    plt.show()    # 図を表示する

    

    # カーソルの切断
    cur.close()

    # コネクションの切断
    conn.close()

if __name__ == "__main__":
    main()
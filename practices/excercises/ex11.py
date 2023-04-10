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
    cur.execute(f"select * from nagoya_population")
    # cur.execute(query)
    
    rows = cur.fetchall()

    years = [i[1] for i in rows]
    # population = [i[2] for i in rows]
    elderly = [i[3] for i in rows]
    young_old = [i[4] for i in rows]
    old_old = [i[5] for i in rows]

    plt.rcParams["font.family"] = "MS Gothic"
    plt.xlabel("年")    # x軸のラベル
    plt.ylabel("人口(人)")    # y軸のラベル
    plt.plot(years, elderly, marker="o", linestyle = "-", label = "高齢者") 
    plt.plot(years, young_old, marker="o", linestyle = "-", label = "前期高齢者")
    plt.plot(years, old_old, marker="o", linestyle = "-", label = "後期高齢者")
    plt.xticks(years) 
    plt.legend(loc = "upper left")    # 凡例を作る
    plt.show()       # 表示する

    

    # カーソルの切断
    cur.close()

    # コネクションの切断
    conn.close()

if __name__ == "__main__":
    main()
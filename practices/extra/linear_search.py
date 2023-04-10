import csv

poke_list = list(csv.reader(open("test\extra\poke.csv", "r")))
poke_list = list(zip(list(range(1,len(poke_list))),poke_list))

# print(poke_list[0])

def lin_search(array, key=""):
    step = 0
    for i in array:
        step += 1
        if i[1][0] == key:
            print(f"{i[1][0]}はリストに存在します。")
            print(i)
            print(f"見つかるまで{step}回探しました。")
            return True
    print(f"{key}はリストに存在しません。")
    return False

def bin_search(array=[], key=""):
    temp_array = sorted(array, key=lambda x:x[1])
    step = 0
    left = 0
    right = len(array)
    while left<=right:
        step += 1
        mid = (left+right)//2
        temp = temp_array[mid]
        if key == temp[1][0]:
            print(f"{temp[1]}はリストに存在します。")
            print(temp)
            print(f"見つかるまで{step}回探しました。")
            return True
        elif temp[1][0] < key:
            left = mid+1
        else:
            right = mid-1
    print(f"{key}はリストに存在しません。")  
    return False


def word_input():
    while 1:
        try:
            user_in = input("探したいポケモンの名前を入力してください。\n終了したい場合は\"end\"と入力してください。")
            return user_in
        except Exception:
            print("なぜ例外が発生したか、明日まで考えといてください。")

def main():
    while 1:
        keyword = word_input()
        if keyword==str.lower("end"):
            quit()
        print("--線形探索の場合--")        
        lin_search(poke_list, keyword)
        print("--二分探索の場合--")
        bin_search(poke_list, keyword)


if __name__ == "__main__":
    main()


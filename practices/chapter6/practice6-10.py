def foo(num, symbol):
    return symbol * num

def bar(array):
    cnt =1
    array2 = []
    for i in range(len(array)):
        if cnt == 1:
            array2.append("○")
            cnt +=1
        if cnt == 2:
            array2.append("△")
            cnt +=1
        if cnt == 3:
            array2.append("□")
            cnt +=1
        if cnt == 4:
            array2.append("×")
            cnt = 1
    return array2
    

def user_input(array):
    while 1:
        try:
            number = int(input("数値を入力(0で終了): "))
            if number == 0:
                return array
            array.append(number)
        except Exception:
            print("無効な値です。")

def main():
    nums =[]
    nums = user_input(nums)
    symbols = bar(nums)
    stars = list(map(foo,nums,symbols))
    print(nums)
    print(stars)


if __name__ == "__main__":
    main()
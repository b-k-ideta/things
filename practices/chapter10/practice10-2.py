import random


def input_student(lst: list):
    while 1:
        name = input("生徒の名前を入力してください。（空白で終了）>>>")
        if name == "":
            return lst
        lst.append(name)


def name_gen(tup: tuple):
    array = list(tup)
    random.shuffle(array)
    for i in array:
        yield i


def input_interface(tup):
    gen = name_gen(tup)
    count = 0
    while 1:
        try:
            choices = int(input("1:生徒の選択\t2:終了>>>"))
            if choices == 1:
                if count < len(tup):
                    print(next(gen))
                    count += 1
                else:
                    count = 0
                    gen = name_gen(tup)
                    print(next(gen))
                    count += 1

            elif choices == 2:
                return
            else:
                print("再度入力してください。")
        except Exception as err:
            print(err)


def main():
    student_list = []
    input_student(student_list)
    student_list = tuple(student_list)
    print(type(student_list), student_list)
    input_interface(student_list)


if __name__ == "__main__":
    main()

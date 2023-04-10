def add(num1, num2):
    result = num1 + num2
    print_form(num1, num2, result, "add")
    return result


def sub(num1, num2):
    result = num1 - num2
    print_form(num1, num2, result, "sub")
    return result


def mul(num1, num2):
    result = num1 * num2
    print_form(num1, num2, result, "mul")
    return result


def div(num1, num2):
    if num2 == 0:
        print("0除算はできません。")
        return None
    result = num1 / num2
    print_form(num1, num2, result, "div")
    return result

# 数式表示用関数
# 4番目の引数で設定された演算子によって表示を変える
def print_form(num1, num2, result, type="none"):
    operator = {"add": "+", "sub": "-", "mul": "*", "div": "/", "none": " "}
    return print(f"{num1} {operator[type]} {num2} = {result}")

def input_to_hex(color):
    while 1:
        try:
            user_in = int(input(f"{color}の値>>>"))
            if user_in in range(0,256):
                if user_in < 16:
                    return str.upper("0"+hex(user_in)[2:])
                return str.upper(hex(user_in)[2:])
            else:
                print("0-255の数字を入力してください。")
        except Exception as err:
            print(err)


# R = int(input("Rの値>>>"))
# G = int(input("Gの値>>>"))
# B = int(input("Bの値>>>"))

R = input_to_hex("R")
G = input_to_hex("G")
B = input_to_hex("B")

# print(f"#{str.upper(hex(R)[2:])}{str.upper(hex(G)[2:])}{str.upper(hex(B)[2:])}")
print(f"#{R+G+B}")



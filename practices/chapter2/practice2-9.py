print("10進数のカラーコード")
code10 = (12, 120, 200)
print(code10)

print("16進数のカラーコード")
"""無駄が多かったのでコメントアウト
 print("#", hex(code10[0])[2:], hex(code10[1])[2:],
       hex(code10[2])[2:], sep="")"""
print("#" + hex(code10[0])[2:] + hex(code10[1])[2:] +
      hex(code10[2])[2:])
    
print(int(0b11111111) )


"""変数に入れる必要なかったのでコメントアウト
a, b, c = code10
print("#", hex(a)[2:],hex(b)[2:],hex(c)[2:], sep="")"""



from pen import Pen

pen1 = Pen("赤",5)
print(pen1)
pen1.draw("こんにちは")

pen2 = Pen()
for i in range(15):
    pen2.draw("こんばんは")
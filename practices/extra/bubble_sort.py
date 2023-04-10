import random
import time

num = list(range(10000))
random.shuffle(num)

print(num)

def bubble(list):
    i = len(num)
    while i != 0:
        flag = False
        for j in range(i-1):
            if num[j]>num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j + 1] = temp
                flag = True
        if flag == True:
            i = i - 1
            j = 0
        else:
            return list
    return list

start = time.time()
num = bubble(num)
elapsed_time = time.time() - start
for i in range(len(num)):
    print(i, "",end="")
    if (i+1)%10==0:
        print()
print("\n処理時間", elapsed_time)  
    
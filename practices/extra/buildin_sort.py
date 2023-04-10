import random
import time

num = list(range(1000))
random.shuffle(num)
# num = [5,1,3,2,4,0,6,7]
print(num)

start = time.time()
list.sort(num)
elapsed_time = time.time() - start
for i in range(len(num)):
    print(i, "",end="")
    if (i+1)%10==0:
        print()
print("\n処理時間", elapsed_time)  
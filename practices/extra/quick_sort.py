import random
import time

num = list(range(20))
random.shuffle(num)

print(num)

def quick_sort(lst):
    left =[]
    right =[]
    if len(lst) <=1:
        return lst
    else:
        pivot = lst.pop()
        for i in lst:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        pivot = [pivot]
        return quick_sort(left) + pivot + quick_sort(right)





start = time.time()
num = quick_sort(num)
elapsed_time = time.time() - start
for i in range(len(num)):
    print(num[i], "",end="")
    if (i+1)%10==0:
        print()
print("\n処理時間", elapsed_time)  

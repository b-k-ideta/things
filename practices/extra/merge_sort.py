import random
import time

num = list(range(1000))
random.shuffle(num)
# num = [5,1,3,2,4,0,6,7]
print(num)

def merge_sort(list_in):
    temp1 =[]
    temp2 =[]
    
    if len(list_in) <= 1:
        return list_in
    else:
        mid = len(list_in)//2
        for i in range(0, mid):
            temp1.append(list_in[i])
        for i in range(mid, len(list_in)):
            temp2.append(list_in[i])
        # print("一時処理用左",temp1)
        # print("一時処理用右",temp2)
        left = merge_sort(temp1)
        right = merge_sort(temp2)

        # print("分割",left, right)
        return merge(left, right)

def merge(left, right):
    lst = []
    i = 0
    j = 0
    while (i<len(left)) and (j<len(right)):
        if left[i] <= right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
    for el in range(i, len(left)):
        lst.append(left[el])
    for el in range(j, len(right)):
        lst.append(right[el])
    # print("統合",lst)
    return lst
    
start = time.time()
num = merge_sort(num)
elapsed_time = time.time() - start
for i in range(len(num)):
    print(i, "",end="")
    if (i+1)%10==0:
        print()
print("\n処理時間", elapsed_time)  

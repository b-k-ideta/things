nums = [4,3,7,6,2,1]


doubler = lambda lst: list(map(lambda x:x*2, lst))

sigma = lambda x: x if x==1 else x + sigma(x-1)

nums2 = doubler(nums)

print(nums)
print(nums2)
print(sigma(100))
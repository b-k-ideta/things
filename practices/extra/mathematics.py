
# 階乗計算
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n -1)


def sigma(n):
    if n < 1:
        return n
    else:
        return n + sigma(n-1)


print(sigma(100))
print(factorial(7))

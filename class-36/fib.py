import time

# Time O(2^n)
# Space O(n)

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fib_iter(n):
    prev = 0
    sum = 1
    for i in range(n):
      temp = sum + prev
      prev = sum
      sum = temp
    return sum

# def fib_memo(n):
#     prev = 0
#     sum = 1
#     for i in range(n):
#       temp = sum + prev
#       prev = sum
#       sum = temp
#     return sum

start = time.time()
fib_iter(35)
total = time.time() - start
print(total)

start = time.time()
fib(35)
total = time.time() - start
print(total)

# print(fib(10))
# print(fib_iter(10))
# assert fib(17) == fib_iter(17)
# print("seems legit")
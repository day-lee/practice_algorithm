#1 Fibonacci Sequence
# return Nth fibonacci number
def fib(n):
    if n <= 2:
        return 1
    return fib(n-2) + fib(n-1)

# Test: print from fib(1) to fib(10)
for i in range(1, 11):
    print(fib(i))

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

#2 Triangle Number
# Return sum of 1 to n
def triangle_number(n):
    if n == 1:
        return 1
    return triangle_number(n-1) + n

# Test: print triangle_number(1) to triangle_number(10)
for i in range(1, 11):
    print(triangle_number(i))

# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55
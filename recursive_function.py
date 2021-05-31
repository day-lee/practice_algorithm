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

#3 Sum of Digits
# retuns sum of each digits, which is parameter 'n'
def sum_digits(n):
    if n < 10:
        return n
    string = str(n)
    return int(string[0]) + sum_digits(int(string[1:]))

# test
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 14
# 15
# 16
# 11
# 20

# suggested solution
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)

print(sum_digits(22541))

#4 Flipped list
# returns flipped list of parameter some_list
def flip(some_list):
    if len(some_list) <= 1:
        return some_list

    return [some_list[-1]] + flip(some_list[0:-1])


# test
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

#[9, 8, 7, 6, 5, 4, 3, 2, 1]
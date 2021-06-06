#Recursive function
'''
Approach
Base case: problem is small enough to solve
Recursive case: Sub-problem exists, can be divided into smaller, recursive case
'''

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

#5 Binary search with recursive function
def binary_search(element, some_list, start_index=0, end_index=None):
    # when end_index is not allocated, use last index from the list
    if end_index == None:
        end_index = len(some_list) - 1

    mid_index = (start_index + end_index) // 2

    #Base case
    if some_list[mid_index] == element:
        return mid_index
    elif end_index - start_index == 0 and some_list[mid_index] != element:
        return None

    #Recursive case
    if some_list[mid_index] > element:
        return binary_search(element, some_list, end_index=mid_index)
    elif some_list[mid_index] < element:
        return binary_search(element, some_list, start_index=mid_index + 1)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

# 0
# None
# 2
# 1
# 4

#suggested solution
def binary_search(element, some_list, start_index=0, end_index=None):
    # when end_index is not allocated, use last index from the list
    if end_index == None:
        end_index = len(some_list) - 1

    # if start_index is bigger than end_index, there is no element in some_list
    if start_index > end_index:
        return None

    # find mid_index from the range
    mid = (start_index + end_index) // 2

    # check if mid index matches with element
    if some_list[mid] == element:
        return mid

    # if element is smaller than mid_index value, search the left side of the list
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # if bigger, search right side
    else:
        return binary_search(element, some_list, mid + 1, end_index)


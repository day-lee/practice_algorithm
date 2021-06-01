# Binary search

#retuns index of element, if it's in some_list
def binary_search(element, some_list):
    first = 0
    end = len(some_list) - 1
    for item in range(len(some_list)):
        mid_index = (first + end) // 2
        if some_list[mid_index] == element:
            return mid_index
        else:
            if some_list[mid_index] > element:
                end = mid_index
            elif some_list[mid_index] < element:
                ''' when dividing the case, mid_index doesn't need to be included
                imagine a linear block and chop it from left or right depending on the location of element'''
                # if some_list[mid_index + 1] == element:
                #     return mid_index + 1
                # else:
                #     first = mid_index
                first = mid_index + 1
    return None

#test
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
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

# others solution
def binary_search(element, some_list):
    index = len(some_list) // 2

    for i in range(len(some_list)):
        if some_list[index] == element:
            return index
        elif some_list[index] > element:
            index = index // 2
        elif some_list[index] < element:
            index = (index + len(some_list)) // 2
    return None
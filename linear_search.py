#1. linear search
# returns index of element if it's in some_list, if not, return None

def linear_search(element, some_list):
    i = 0
    while i < len(some_list):
        if element == some_list[i]:
            return i
        i += 1

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

# 0
# None
# 2
# 1
# 4
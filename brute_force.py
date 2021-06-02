#Brute Force

#returns the biggest number when choosing cards from each side and multiply
def max_product(left_cards, right_cards):
    new_list = []
    for left in left_cards:
        for right in right_cards:
            all_list = left * right
            new_list.append(all_list)
    return max(new_list)


# test
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

# 24
# 32
# 28
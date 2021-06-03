#Brute Force

#1 Cards combination 카드 뭉치 최대 조합
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

#2 closest stores 가까운 매장 찾기
# import sqrt function for square root (제곱근)
from math import sqrt

#returns straight distance between two stores
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# returns the closest two stores
def closest_pair(coordinates):
    min_distance = 1000
    for store1 in test_coordinates:
        for store2 in test_coordinates:
            if distance(store1, store2) != 0.0:
                min_distance = min(min_distance, distance(store1, store2))
        # return min_distance
        return [store1, store2]

# test
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

# [(2, 3), (3, 4)]

# suggested solution
''' 
1. subtracted and added 1 in for loop as some overlaps when using brute force
2. two variables assigned in one line e.g. line 69 
'''

# 제곱근 사용을 위한 sqrt 함수 불러오기
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair

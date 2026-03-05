# 127
# numbers = [46, 23, -52, 34, 6, -18, 52]
# plan:
# 1. eng kichik element = min
# 2. manfiy elementlarini topish
# 3. m.elementlarini min ** 2 ga almashtirish => numbers[2] = 23
# min_value = min(numbers)
# for index in range(len(numbers)):
#     if numbers[index] < 0:
#         numbers[index] = min_value ** 2

# print(*numbers)

# 110
# nums = [7, 11, 83, 18, 31]
# K = int(input("K sonini kiriting: "))
# M = int(input("M sonini kiriting: "))
# k = 1
# for son in nums:
#     if son == K or son == M:
#         k *= son
# print(k) 

# 104
# plan:
# 1. min element topish
# 2. oxirgi element topish
# 3. almashtirish
# sonlar = [74, 0, 1, 33] 
# minimum_value = min(sonlar)
# last_element = sonlar[-1]
# min_index = sonlar.index(minimum_value)

# sonlar[min_index] = last_element
# sonlar[-1] = minimum_value
# print(sonlar)

# 124
# numbers = [29, 50, -14, 4, 27, -56]
# k = int(input("Element o'rnini kiriting: "))
# plan:
# 1. max element topish
# 2. max element indexini topish
# 3. k o'rindagi element bilan max element o'rnini almashtirish
# max_value = max(numbers)
# max_index = numbers.index(max_value)
# numbers[4] = 32
# numbers[max_index] = numbers[k - 1]
# numbers[k - 1] = max_value
# print(numbers)

a, b = 5, 3
# natija: a = 3; b = 5
# 1-usul:
# temporary variable - vaqtinchalik o'zgaruvchi
# c = a # 5
# a = b # 3
# b = c # 5
# print(a, b)

# 2-usul:
# a, b = b, a
# print(a, b)

# 3-usul:
[a, b] = [b, a]
print(a, b)
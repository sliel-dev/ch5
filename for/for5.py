# dic = {'apple':1200, 'banana':800, 'orange':1500}

# for k in dic.keys():
#     print(k)
# for v in dic.values():
#     print(v)

# for k, v in dic.items():
#     print(k)
#     print(v)

# for n in range(10):
#     print(n)

# for n in range(10):
#     print('hi')

# scores = {'철수' : 80, '영희' : 95, '민수' : 70, '지연' : 100}
# v = 0
# for n in scores.values():
#     v = v + n
# print(v / len(scores))

# for k, v in scores.items():
#     s = 0
#     s = s + v
#     if s > 90:
#         print(k)
#         continue

# nums = [1, 2, 3, 4]
# new_nums = []
# for n in nums:
#     new_nums.append(n * 3)

# new_nums = [n * 3 for n in nums]
# print(new_nums)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 리스트 = [변수 + for + if]
# n_nums = [n for n in nums if n % 2 == 0]
# for n in nums:
#     if n % 2 == 0:
#         n_nums.append(n)
#         continue
# print(n_nums)

strings = ['a', 'bb', 'ccc', 'dddd', 'e']

n_str = [n.upper() for n in strings if len(n) > 2]

# for n in strings:
#     if len(n) > 2:
#         n_str.append(n.upper())
#         continue
print(n_str)
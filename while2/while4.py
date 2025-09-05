i = 0
# while i <= 10:
#     if i % 2 == 0:
#         i+=1
#         continue
#     print(i)
#     i+=1

lis = [10, 'a', True, 20, 'b']

while i < len(lis):
    if type(lis[i]) == str:
        i+=1
        continue
    print(lis[i])
    i+=1
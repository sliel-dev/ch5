lis = [100, 77, -5, 10]
i = 0
# while i <= len(lis) -1:
#     if lis[i] >= 0 :
#         print(lis[i])
#         i+=1
#         continue
#     i+=1

while i <= len(lis) -1:
    if lis[i] == 77 :
        print('이유 :', lis[i], '종료값 출현')
        break
    print(lis[i])
    i+=1
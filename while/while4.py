i = 1
sum = 0
while i <= 20:
    sum = sum + i
    if sum > 100:
        print(sum)
        print(i)
        break
    i+=1
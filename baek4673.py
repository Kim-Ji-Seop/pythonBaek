def d(n):
    sum=0
    main_num = n
    while n > 0 :
        temp = n % 10
        sum = sum + temp
        n = n // 10
    return main_num + sum

arr = [0] * 10001

for i in range(1,10000):
    if d(i) > 10000:
        continue
    else:
        arr[d(i)] += 1

for a in range(1,10000):
    if arr[a] == 0:
        print(a)
    
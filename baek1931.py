import sys
input = lambda : sys.stdin.readline().rstrip()
B =int(input())
arr = [0 for _ in range(B) ]
max=0
for i in range(B):    
	arr[i] = list(map(int, input().split()))

arr.sort()

for i in range(len(arr)):
    count=1
    endT = arr[i][1]
    for j in range(len(arr)-1):
        startT = arr[j+1][0]
        if endT <= startT:
            endT = arr[j+1][1]
            count += 1
    if max <= count:
        max = count
############
print(max)

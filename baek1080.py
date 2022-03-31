import sys

n,m = map(int, sys.stdin.readline().split())
test_number = n // 3
a_list = [list(map(int, input())) for _ in range(n)]
b_list = [list(map(int, input())) for _ in range(n)]

print(a_list)# [세로][가로]
print(b_list)

for i in range(n):
    for j in range(m):
        
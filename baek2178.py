from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

X = [-1,1,0,0]
Y = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]

print(BFS(0,0))

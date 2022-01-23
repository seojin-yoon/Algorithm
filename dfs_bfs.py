#백준 1260번
n,m,v = map(int, input().split())
adjMatrix = [[0] * (n + 1) for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
for i in range(m):
    x,y = map(int, input().split())
    adjMatrix[x][y] = 1
    adjMatrix[y][x] = 1

def DFS(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and adjMatrix[v][i] == 1:
            DFS(i)
def BFS(v):
    queue = [v]
    visited[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visited[i] == 1 and adjMatrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0
    
DFS(v)
print()
BFS(v)

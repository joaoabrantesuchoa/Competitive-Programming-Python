def DFS(graph,v):
    visited[v] = 0
    for s in graph[v]:
        if visited[s] == -1:
            visited[s] = 0
            DFS(graph,s)

n,m = input().split()
n = int(n)
m = int(m)
contador_linhas = m
adj = []
visited = []
for x in range(n+2):
    visited.append(-1)
for x in range(n+2):
    adj.append([])
while contador_linhas != 0:
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
    contador_linhas -= 1
print(adj)
DFS(adj, 1)
if visited.count(0) == n:
    if m == n - 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


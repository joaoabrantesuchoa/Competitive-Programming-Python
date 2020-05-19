INF = 1e10

n, m = map(int,input().split())


d = [[INF]*n for i in range(n)]

for x in range(m):
    a,b,w = map(int,input().split())

    d[a-1][b-1] = w
    d[b-1][a-1] = w
    d[a-1][a-1] = 0
    d[b-1][b-1] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d)



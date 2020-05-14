'''
----COMPLEXIDADE----
Pré-processar a árvore: O(NlogN)
Cada query: O(logN)
'''
import math

n = int(input())

def dfs (v,p): #Faz a dfs na árvore para construir a array up e os tempos
    global timer
    timer += 1
    tin[v] = timer
    up[v][0] = p
    for i in range(1,L + 1):
        up[v][i] = up[up[v][i-1]][i-1]

    for u in adj[v]:
        if u != p:
            dfs(u,v)

    timer += 1
    tout[v] = timer


def is_ancestor(u,v):
    return tin[u] <= tin[v] and tout[u] >= tout[v]

def lca(u,v):

    if is_ancestor(u,v):
        return u
    if is_ancestor(v,u):
        return v

    i = L
    while i >= 0:
        if is_ancestor(up[u][i],v) is False:
            u = up[u][i]
        i -= 1

    return up[u][0]




adj = [[] for i in range(n)]

for x in range(n-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

tin = [0] * n
tout = [0] * n
timer = 0
L = math.ceil(math.log2(n))
up = [[L+1] * (n-1) for i in range(n)]


dfs(0,0)
print(lca(3,4))
print(lca(1,3))
print(lca(4,1))
print(lca(1,2))





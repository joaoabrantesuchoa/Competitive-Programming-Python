def make_set(v):
    parent[v] = v
    size[v] = 1

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]

def union_set(a,b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if size[a] < size[b]:
            a,b = b,a
        parent[b] = a
        size[a] += size[b]




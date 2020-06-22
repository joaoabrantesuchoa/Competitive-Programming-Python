n = int(input())
arr = list(map(int,input().split()))
tree = [0] * (4 * n)

def build(no,l,r): #inicial. no = 1(representa o topo da arvore) l = 1e r = n:
    if l == r:
        tree[no] = arr[l]

    else:
        mid = (l+r) >> 1

        build(no << 1, l , mid)
        build(no << 1|1, mid + 1, r)

        tree[no] = tree[no << 1] + tree[no << 1|1]

def update(no,l,r,pos,val):#Segue até as folhas, muda o valor delas e vai atualizando no caminho de volta até ao topo.
    if l == r:
        tree[no] += val
        #tree[no] = val para caso queira mudar ao invés de incrementar

    else:
        mid = (l+r) >> 1

        if pos <= mid:
            update(no << 1, l, mid, pos,val) #atualiza o filho da esquerda

        else:
            update(no << 1|1, mid + 1, r, pos, val) #Atualiza o filho da direita

        tree[no] = tree[no << 1] + tree[no << 1|1]


def query(no,l,r,x,y):#query de soma 
    if x <= l and r <= y:#O segmento que eu quero está contido no segmento atual
        return tree[no]

    elif (l > y or r < x): #O segmento que eu quero não está contido
        return 0

    else: #O segmento que eu quero está parcialmente contido.
        mid = (l + r) >> 1

        return query(no << 1, l, mid, x, y) + query(no << 1|1, mid + 1, r, x, y)

'''Para construir a segmeent tree, nos vamos criar uma array de somas.
Nesse array, cada index representa a soma de um partido da raiz e seus filhos consecutivos, 
no caso da array A = [4,5,6], significa que a soma da raiz está no indíce 0, 
a soma dos seus filhos estão nos indices 1 e 2, a soma dos filhos dos filhos estão nos indices 3,4,5,6 e assim por diante.

Partindo desse princípio, é visível que o child node do lado esquerdo de um nó de index I é 2I, 
enquanto o child node do lado direito do mesmo nó de index I é 2I + 1.

No pior caso, o tamanho da array será 4N(N é o número de vertices)
'''

N = int(input())
array = list(map(int,input().split()))

segment_tree = [0] * (4 * N)

''' 
A função que constroi a segment tree recebe quatro parâmetros,  
a array A(input array), v(o index do vértice atual), TL e TR(os limites do segmento atual). 
No caso do vértice raiz, v= 1, tl = 0 tr = N - 1.
'''
def build(array, v, tl, tr):
    if tl == tr:
        segment_tree[v] = array[tl]
    else:
        tm = (tl + tr) // 2
        build(array, v * 2, tl, tm)
        build(array, (v * 2) + 1, tm + 1, tr)
        segment_tree[v] = segment_tree[v*2] + segment_tree[(v*2) + 1]

''' A função soma das queries tem como parâmetros as informações sobre o segmento atual(index v e limites tl e tr) 
além dos limites da query l e r. 
'''

def soma_queries(v,tl,tr,l,r):
    if (l > r):
        return 0
    if (l == tl and r == tr):
        return segment_tree[v]
    tm = (tl + tr) // 2
    return soma_queries(v * 2, tl, tm, l, min(r,tm)) + soma_queries((v * 2) + 1, tm + 1, tr, max(l, tm + 1), r)


''' A função update recebe as informações do vértice atual e dos novos valores que ele possuirá'''

def update(v,tl,tr,pos,new_val):
    if (tl == tr):
        segment_tree[v] = new_val
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(v*2, tl, tm, pos, new_val)
        else:
            update((v*2) + 1, tm + 1, tr, pos, new_val)
        segment_tree[v] = segment_tree[v*2] + segment_tree[(v*2)+1]


build(array,1,0,N-1)
soma = soma_queries(1,0,N-1,1,3)
print(soma)

    
'''
Código adaptado de CP Algorithms:
    
    https://cp-algorithms.com/data_structures/segment_tree.html

Todos os direitos reservados ao site
'''

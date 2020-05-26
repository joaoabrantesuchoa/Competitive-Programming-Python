INF = 1e10

n, m = map(int,input().split())

distancia = [[INF]*n for i in range(n)]
'''
grafo = []
for i in range(n):
    lista = []
    for j in range(n):
        if i == j:
            lista.append(0)
        else:
            lista.append(INF)
    grafo.append(lista)
    
for x in range(m):
    no1,no2,peso = map(int,input().split())
    if peso < grafo[no1][no2]:
        grafo[no1][no2] = peso

'''

for x in range(m):
    no1,no2,peso = map(int,input().split())

    d[no1-1][no2-1] = peso
    d[no2-1][no1-1] = peso
    d[no1-1][no1-1] = 0
    d[no2-1][no2-1] = 0

def floyd(): #Apenas para pesos positivos
    for fase in range(n):
        for saida in range(n):
            for chegada in range(n):
                distancia[saida][chegada] = min(distancia[saida][chegada], distancia[saida][fase] + distancia[fase][chegada])

def floyd_negativo(): #pesos positivos e negativos
    for fase in range(n):
        for saida in range(n):
            for chegada in range(n):
                if distancia[saida][fase] < INF and distancia[fase][chegada] < INF:
                    distancia[saida][chegada] = min(distancia[saida][chegada], distancia[saida][fase] + distancia[fase][chegada])
                
                
def encontrar_ciclo(): #Basicamente você verifica se a distância do nó para si mesmo é menor do que 0, se for tem ciclo
    for fase in range(n):
        for saida in range(n):
            chegada = 0
            while distancia[fase][saida] != -INF and chegada < n: #Esses distancia != INF é só para verificar se é possível alcançar o nó, senão o algoritmo pode ir atrás de caminho que não existe.
                if distancia[chegada][chegada] < 0 and distancia[fase][chegada] != INF and distancia[chegada][saida] != INF:
                    distancia[fase][chegada] = -INF  #Coloca-se -INF para implicar uma menor distância infinita 
                chegada += 1

def verificar_presenca_ciclo(): #Só olha se tem ciclo negativo ou não, não coloca a distancia dele ou outra coisa, só olha
    for no in range(n):
        if distancia[no][no] < 0:
            return True

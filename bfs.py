from multiprocessing import Pool, Manager
from grafo import grafo  # Importa o grafo gerado
from time import perf_counter
from collections import deque  # Importação do deque

def dfs_iterativo(grafo, inicio, visitados, componente):
    pilha = [inicio]
    while pilha:
        no = pilha.pop()
        if no not in visitados:
            visitados.add(no)
            componente.append(no)
            pilha.extend(grafo.get(no, []))

def encontrar_componentes_conexas(grafo):
    visitados = set()
    componentes = []

    for no in grafo:
        if no not in visitados:
            componente = []
            dfs_iterativo(grafo, no, visitados, componente)
            componentes.append(componente)

    return componentes

def bfs_subgrafo(args):
    grafo, inicio, visitados_compartilhado = args
    fila = deque([inicio])  # Usando deque

    while fila:
        vertice = fila.popleft()  # O(1) com deque
        if vertice not in visitados_compartilhado:
            print(f"[{inicio}] Visitando: {vertice}")
            visitados_compartilhado.append(vertice)
            for vizinho in grafo.get(vertice, []):
                if vizinho not in visitados_compartilhado and vizinho not in fila:
                    fila.append(vizinho)

def bfs(grafo, number_of_workers=1):
    manager = Manager()
    visitados = manager.list()
    
    componentes = encontrar_componentes_conexas(grafo)

    argumentos = [(grafo, next(iter(componente)), visitados) for componente in componentes]

    with Pool(processes=number_of_workers) as pool:
        pool.map(bfs_subgrafo, argumentos)

    print("\nTodos os nós visitados:", list(visitados))

if __name__ == "__main__":
    start = perf_counter()
    # bfs(grafo, 1)  # Usa 1 processos
    bfs(grafo, 2)  # Usa 2 processos
    end = perf_counter()

    print(f"Tempo de execução: {end - start:.6f} segundos")

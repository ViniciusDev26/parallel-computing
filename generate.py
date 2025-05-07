import random

def gerar_e_salvar_grafo_grande(caminho_arquivo, num_nos=500, conexoes_por_no=3):
    with open(caminho_arquivo, "w") as f:
        f.write("grafo = { \n")
        for i in range(num_nos):
            no = f"N{i}"
            vizinhos = set()
            while len(vizinhos) < conexoes_por_no:
                vizinho_idx = random.randint(0, num_nos - 1)
                if vizinho_idx != i:
                    vizinhos.add(f"N{vizinho_idx}")
            linha = f"'{no}': {list(vizinhos)},\n"
            f.write(linha)
        f.write("}")

gerar_e_salvar_grafo_grande("grafo.py")

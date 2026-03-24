import sys
import os
from graph import Graph
from breadth_first_paths import BreadthFirstPaths

estados = {
    0: 'AL', 1: 'BA', 2: 'CE', 3: 'MA', 
    4: 'PB', 5: 'PE', 6: 'PI', 7: 'RN', 8: 'SE'
}
    
siglas_para_id = {sigla: id_v for id_v, sigla in estados.items()}

caminho_arquivo = os.path.join('trabalho-bfs-dfs','dados', 'nordeste.txt')
    
with open(caminho_arquivo, 'r') as f:
         
    num_vertices = int(f.readline().strip())
    num_arestas = int(f.readline().strip())
            
    g = Graph(num_vertices)
            
    for _ in range(num_arestas):
        linha = f.readline().strip()
        if linha: 
            v, w = linha.split()
            g.add_edge(int(v), int(w))
    
origem_input = input("Informe a sigla do estado de ORIGEM: ").strip().upper()
destino_input = input("Informe a sigla do estado de DESTINO: ").strip().upper()

if origem_input not in siglas_para_id or destino_input not in siglas_para_id:
    print("Erro: Sigla de estado inválida. Tente novamente.")
    sys.exit(1)

origem = siglas_para_id[origem_input]
destino = siglas_para_id[destino_input]

bfs = BreadthFirstPaths(g, origem)

caminho_ids = bfs.path_to(destino)
caminho_siglas = [estados[v] for v in caminho_ids]
        
print(f"Origem: {origem_input}")
print(f"Destino: {destino_input}")
print(f"Caminho: {' -> '.join(caminho_siglas)}")
print(f"Quantidade de fronteiras a cruzar: {len(caminho_siglas) - 1}")

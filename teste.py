from meu_grafo import MeuGrafo

paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

paraiba.adicionaAresta('a1', 'J', 'C')
paraiba.adicionaAresta('a2', 'C', 'E')
paraiba.adicionaAresta('a3', 'C', 'E')
paraiba.adicionaAresta('a4', 'P', 'C')
paraiba.adicionaAresta('a5', 'P', 'C')
paraiba.adicionaAresta('a6', 'T', 'C')
paraiba.adicionaAresta('a7', 'M', 'C')
paraiba.adicionaAresta('a8', 'M', 'T')
paraiba.adicionaAresta('a9', 'T', 'Z')



r = 'C'
dfs_paraiba = MeuGrafo([r])
bfs_paraiba = MeuGrafo([r])
#print(paraiba.nova_dfs(bfs_paraiba, r))
#print(paraiba.bfs(dfs_paraiba, r))

teste = MeuGrafo(list('1234'))

teste.adicionaAresta('a1', '1', '2')
teste.adicionaAresta('a2', '2', '3')
teste.adicionaAresta('a3', '3', '4')
teste.adicionaAresta('a4', '4', '1')
teste.adicionaAresta('a5', '1', '4')

raiz = '1'
dfs = MeuGrafo([raiz])
#print(teste.nova_dfs(dfs, raiz))


grafo_atv = MeuGrafo(list('ABCDEFGHIJK'))

grafo_atv.adicionaAresta('a1', 'A', 'B')
grafo_atv.adicionaAresta('a2', 'B', 'C')
grafo_atv.adicionaAresta('a3', 'C', 'D')
grafo_atv.adicionaAresta('a4', 'D', 'E')
grafo_atv.adicionaAresta('a5', 'E', 'B')
grafo_atv.adicionaAresta('a6', 'B', 'F')
grafo_atv.adicionaAresta('a7', 'F', 'H')
grafo_atv.adicionaAresta('a8', 'H', 'G')
grafo_atv.adicionaAresta('a9', 'G', 'B')
grafo_atv.adicionaAresta('a10', 'G', 'A')
grafo_atv.adicionaAresta('a11', 'G', 'K')
grafo_atv.adicionaAresta('a12', 'G', 'J')
grafo_atv.adicionaAresta('a13', 'G', 'I')
grafo_atv.adicionaAresta('a14', 'A', 'J')
grafo_atv.adicionaAresta('a15', 'J', 'K')
grafo_atv.adicionaAresta('a16', 'J', 'I')

grafo_sem_ciclo = MeuGrafo(list('ABCDEFGHIJK'))
grafo_sem_ciclo.adicionaAresta('a1', 'A', 'J')
grafo_sem_ciclo.adicionaAresta('a2', 'A', 'G')
grafo_sem_ciclo.adicionaAresta('a3', 'A', 'B')
grafo_sem_ciclo.adicionaAresta('a4', 'J', 'K')
grafo_sem_ciclo.adicionaAresta('a5', 'J', 'I')
grafo_sem_ciclo.adicionaAresta('a6', 'G', 'H')
grafo_sem_ciclo.adicionaAresta('a7', 'B', 'F')
grafo_sem_ciclo.adicionaAresta('a8', 'B', 'C')
grafo_sem_ciclo.adicionaAresta('a9', 'B', 'D')
grafo_sem_ciclo.adicionaAresta('a10', 'B', 'E')

raiz = 'A'
dfs = MeuGrafo([raiz])
bfs = MeuGrafo([raiz])

#print("BUSCA E PROFUNDIDADE")
dfs = grafo_atv.nova_dfs(dfs, raiz)
#print("BUSCA E LARGURA")
#print(grafo_atv.bfs(bfs, raiz))

arv_vazia = MeuGrafo()
#print(grafo_atv.ha_ciclo(arv_vazia))
arv_vazia = MeuGrafo()
#print(dfs.ha_ciclo(arv_vazia))

arv_vazia = MeuGrafo()
print(grafo_atv.ha_ciclo2(arv_vazia, 'D'))

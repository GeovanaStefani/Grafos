from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import Counter
import random

class MeuGrafo(GrafoListaAdjacencia):

    #Metodos Private
    def eh_laco(self, a):
        '''Verifica se a aresta passada é um laço.

        :param a: nome da aresta

        :return: True ou False, se a aresta é ou não um laço
        '''
        arestas = self.A

        if arestas[a].getV1() == arestas[a].getV2():
            return True
        return False

    def monta_aresta(self, v1, v2):
        '''Monta uma string com os 2 vértices passados.

        :param v1: Vértice 1
        :param v2: Vértice 2
        :return: 'V1-V2'
        '''
        return v1 + "-" + v2

    def arestas_iguais(self, aresta1, aresta2):
        ''' Verifica se as arestas são ou não iguais

        :param aresta1: Primeira aresta
        :param aresta2: Segunda aresta
        :return: Booleano
        '''
        if (aresta1.getV1() == aresta2.getV1()) and (aresta1.getV2() == aresta2.getV2()):
            return True
        elif (aresta1.getV1() == aresta2.getV2()) and (aresta1.getV2() == aresta2.getV1()):
            return True
        return False

    def arestas_no_grafo(self, arvore):
        ''' Verifica se todas as arestas da árvore passada no parâmetro
        estão na arvore self.

        :param arvore: Arvvore
        :return: Booleano
        '''
        arestas = self.A
        arestas_arvore = arvore.A
        for a in arestas_arvore:
            try:
                if arestas[a] != arestas_arvore[a]:
                    return False
            except KeyError:
                return False
        return True

    def caminho_no_grafo(self, caminho):
        grafo_aux = MeuGrafo([caminho[0]])
        for i in range(0, len(caminho)-1, 2):
            v1 = caminho[i]
            a = caminho[i+1]
            v2 = caminho[i+2]

            if v2 not in grafo_aux.N:
                grafo_aux.adicionaVertice(v2)
            grafo_aux.adicionaAresta(a, v1, v2)

        return self.arestas_no_grafo(grafo_aux)

    def vertice_oposto(self, a, r):
        '''Retorna o vértice oposto ao vértice passado no parâmetro na respectiva aresta

        :param a: aresta a ser verificada
        :param r: verice raiz
        :return: vertice oposto
        '''
        arestas = self.A
        if arestas[a].getV1() == r:
            v = arestas[a].getV2()
        else:
            v = arestas[a].getV1()
        return v

    def paralelas(self, aresta_aux):
        '''Verifica se a aresta passada no parâmetro já existe no grafo,
        indicando se é ou não uma paralela.

        :param aresta_aux: aresta a ser verificada
        :return: Booleano
        '''
        for a in self.A:
            if self.arestas_iguais(aresta_aux, self.A[a]):
                return True
        return False

    def assinatura_busca(self, raiz):
        '''Retorna uma raiz (sorteada ou passada no parâmetro) e um grafo só com o vértice da raiz,
        para serem usados nas funções de busca.

        :param raiz: Vértice inicial
        :return: raiz, grafo([raiz])
        '''
        if not raiz:
            raiz = random.choice(self.N)
        arvore = MeuGrafo([raiz])
        return raiz, arvore

    # Métodos Public

    # Funções Gerais
    def vertices_nao_adjacentes(self):
        '''Provê uma lista de vértices não adjacentes no grafo.
        A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.

        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vertices = self.N
        arestas = self.A
        vertices_nao_adjacentes = set()

        for v1 in vertices:
            adjacentes_vertice_v = []
            for a in arestas:
                if arestas[a].getV1() == v1:
                    adjacentes_vertice_v.append(arestas[a].getV2())
                elif arestas[a].getV2() == v1:
                    adjacentes_vertice_v.append(arestas[a].getV1())

            for v2 in vertices:
                if v1 == v2:
                    continue
                if v2 not in adjacentes_vertice_v:
                    aresta = self.monta_aresta(v1, v2)
                    if self.monta_aresta(v2, v1) not in vertices_nao_adjacentes:
                        vertices_nao_adjacentes.add(aresta)

        return vertices_nao_adjacentes

    def ha_laco(self):
        '''Verifica se existe algum laço no grafo.

        :return: Booleano
        '''
        arestas = self.A

        for i in arestas:
            if self.eh_laco(i):
                return True
        return False

    def grau(self, V=''):
        '''Provê o grau do vértice passado como parâmetro.
        O grau indica em quantas arestas aquele vértice está

        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        vertices = self.N
        arestas = self.A
        grau = 0

        if V not in vertices:
            raise VerticeInvalidoException("Vertíce Inválido!")
        else:
            for i in arestas:
                if arestas[i].getV1() == V:
                    grau += 1
                if arestas[i].getV2() == V:
                    grau += 1
        return grau

    def ha_paralelas(self):
        '''Verifica se há arestas paralelas no grafo.

        :return: Booleano
        '''
        arestas = self.A

        for i in arestas:
            for c in arestas:
                if i == c:  #arestas são iguais
                    continue
                aresta_aux = Aresta(i, arestas[c].getV1(), arestas[c].getV2())
                if arestas[i] == aresta_aux:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro

        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertices = self.N
        arestas = self.A
        arestas_sobre_vertices = set()

        if V not in vertices:
            raise VerticeInvalidoException("Vertíce Inválido!")
        else:
            for i in arestas:
                if (arestas[i].getV1() == V) or (arestas[i].getV2() == V):
                    if i not in arestas_sobre_vertices:
                        arestas_sobre_vertices.add(i)
        return arestas_sobre_vertices

    def eh_completo(self):
        '''Verifica se o grafo é completo.
        Completo é uma definição dada a um grafo simples (sem laços e paralelas),
        que cada vértice esteja conectado com todos os outros.

        :return: Booleano
        '''
        if len(self.vertices_nao_adjacentes()) == 0:
            if not self.ha_laco():
                if not self.ha_paralelas():
                    return True
        return False

    # Chamada dos Algoritmos de Busca
    def dfs(self, raiz=''):
        '''Faz a assinatura da função e retorna a função de busca dfs.
        A dfs é um caminho que passa por todos os vértices através da busca e profundidade.

        :param raiz: Vértice para começar a busca
        :return: grafo dfs
        '''
        raiz, arvore = self.assinatura_busca(raiz)
        return self.busca_dfs(raiz, arvore)

    def bfs(self, raiz=''):
        '''Faz a assinatura da função e retorna a função de busca bfs.
        A bfs é um caminho que passa por todos os vértices através da busca e largura.

        :param raiz: Vértice para começar a busca
        :return: grafo bfs
        '''
        raiz, arvore = self.assinatura_busca(raiz)
        return self.busca_bfs(raiz, arvore)

    def caminho(self, n):
        '''Verifica se existe um caminho de tamanho n.
        Se sim, retorna um desses caminhos. Se não, retorna False

        :param n: Tamanho do caminho
        :return: Caminho:[v1, a1, v2, a2, v3] ou False
        '''
        if n <= len(self.A):
            for v in self.N:
                busca = self.busca_caminho(n, v, 0, [v])
                if busca[1] >= n:
                    return busca[0]
        return False

    def ha_ciclo(self):
        '''Verifica se há um ciclo no grafo.
        Se sim, retorna um desses ciclos. Se não, retorna False

        :return: Caminho:[v1, a1, v2, a2, v1] ou False
        '''
        for v in self.N:
            busca = self.busca_ciclo(v, [v])
            #print('busca completa: ', busca)
            if busca:
                if busca[0] == busca[-1]:
                    return busca

                counter = Counter(busca)
                for c in counter:
                    if counter[c] > 1:
                        inicio = busca.index(c)
                        return busca[inicio:]
        return False

    # Aplicações dos Algoritmos de Busca (dfs e bfs)
    def busca_dfs(self, raiz, arvore):
        '''Faz a busca da dfs de forma recursiva.

        :param raiz: vértice analisado no momento
        :param arvore: árvore que está sendo montada
        :return: arvore dfs
        '''
        arestas_na_raiz = self.arestas_sobre_vertice(raiz)

        for aresta in arestas_na_raiz:
            vertice = self.vertice_oposto(aresta, raiz)
            aresta_aux = Aresta("aux", raiz, vertice)
            if not arvore.existeRotuloAresta(aresta):
                if not arvore.paralelas(aresta_aux):
                    if not arvore.existeVertice(vertice):
                        arvore.adicionaVertice(vertice)
                        arvore.adicionaAresta(aresta, raiz, vertice)
                        self.busca_dfs(vertice, arvore)
        return arvore

    def busca_bfs(self, raiz, arvore):
        '''Faz a busca da bfs de forma recursiva.

        :param raiz: vértice analisado no momento
        :param arvore: árvore que está sendo montada
        :return: arvore bfs
        '''
        arestas_na_raiz = self.arestas_sobre_vertice(raiz)
        validador = False
        for aresta in arestas_na_raiz:
            vertice = self.vertice_oposto(aresta, raiz)
            aresta_aux = Aresta("aux", raiz, vertice)
            if not arvore.existeRotuloAresta(aresta):
                if not arvore.paralelas(aresta_aux):
                    if not arvore.existeVertice(vertice):
                        arvore.adicionaVertice(vertice)
                        arvore.adicionaAresta(aresta, raiz, vertice)
                        validador = True
        if not validador:
            return arvore
        for a in arestas_na_raiz:
            vertice = self.vertice_oposto(a, raiz)
            self.busca_bfs(vertice, arvore)

        return arvore

    def busca_caminho(self, n, v, tam, caminho):
        '''Faz a busca do caminho de tamanho n de forma recursiva.

        :param n: Tamanho do caminho (solicitado)
        :param v: vértice em questão
        :param tam: tamanho do caminho (que está sendo construído)
        :param caminho: caminho que está sendo construído
        :return: caminho de tamanho n
        '''
        if tam == n:
            return caminho, tam

        arestas_no_vertice = self.arestas_sobre_vertice(v)

        for a in arestas_no_vertice:
            o = self.vertice_oposto(a, v)
            if a not in caminho:
                tam += 1
                caminho.append(a)
                caminho.append(o)
                caminho, tam = self.busca_caminho(n, o, tam, caminho)
                if tam == n:
                    return caminho, tam
        caminho.pop()
        if caminho:
            caminho.pop()
            tam -= 1
        return caminho, tam

    def busca_ciclo(self, v, caminho):
        '''Faz a busca do ciclo de forma recursiva

        :param v: vértice atual
        :param caminho: caminho que está sendo construído do ciclo
        :return: caminho com um ciclo
        '''
        if caminho.count(v)>1:
            return caminho

        arestas_no_vertice = self.arestas_sobre_vertice(v)

        for a in arestas_no_vertice:
            o = self.vertice_oposto(a, v)
            if a not in caminho:
                caminho.append(a)
                caminho.append(o)
                caminho = self.busca_ciclo(o, caminho)
                if o in caminho:
                    return caminho
        caminho.pop()
        if caminho:
            caminho.pop()
        return caminho

    def conexo(self):
        '''Verifica se o grafo é ou não conexo.
        Conexo é o grafo que contém um caminho pra chegar em todos os vértices.

        :return: Booleano
        '''
        dfs = self.dfs()
        return set(dfs.N) == set(self.N)

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass
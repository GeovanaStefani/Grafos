from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    #Metodos Private
    def eh_laco(self, a):
        '''
        Verifica se a aresta passada é um laço.

        :param a: nome da aresta
        :return: True ou False, se a aresta é ou não um laço
        '''
        arestas = self.A

        if arestas[a].getV1() == arestas[a].getV2():
            return True
        return False

    def monta_aresta(self, v1, v2):
        '''
        Monta uma string com os 2 vértices passados.

        :param v1: Vértice 1
        :param v2: Vértice 2
        :return: 'V1-V2'
        '''
        return v1 + "-" + v2

    #Metodos Public
    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
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
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        arestas = self.A

        for i in arestas:
            if self.eh_laco(i):
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
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
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
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
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
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
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if len(self.vertices_nao_adjacentes()) == 0:
            if not self.ha_laco():
                if not self.ha_paralelas():
                    return True
        return False

    def vertice_oposto(self, a, r):
        arestas = self.A
        if arestas[a].getV1() == r:
            v = arestas[a].getV2()
        else:
            v = arestas[a].getV1()
        return v

    def arestas_iguais(self, aresta1, aresta2):
        if (aresta1.getV1() == aresta2.getV1()) and (aresta1.getV2() == aresta2.getV2()):
            return True
        elif (aresta1.getV1() == aresta2.getV2()) and (aresta1.getV2() == aresta2.getV1()):
            return True
        return False

    def paralelas(self, aresta_aux):
        for a in self.A:
            if self.arestas_iguais(aresta_aux, self.A[a]):
                return True
        return False

    def nova_dfs(self, arvore, raiz):
        arestas_na_raiz = self.arestas_sobre_vertice(raiz)

        for aresta in arestas_na_raiz:
            vertice = self.vertice_oposto(aresta, raiz)
            aresta_aux = Aresta("aux", raiz, vertice)
            if not arvore.existeRotuloAresta(aresta):
                if not arvore.paralelas(aresta_aux):
                    if not arvore.existeVertice(vertice):
                        arvore.adicionaVertice(vertice)
                        arvore.adicionaAresta(aresta, raiz, vertice)
                        self.nova_dfs(arvore, vertice)
        return arvore

    def bfs(self, arvore, raiz):
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
            self.bfs(arvore, vertice)

        return arvore

    '''def ha_ciclo(self, arvore):
        for r in self.N:
            arestas_na_raiz = self.arestas_sobre_vertice(r)
            for a in arestas_na_raiz:
                if self.eh_laco(a):
                    return True
                vertice = self.vertice_oposto(a, r)
                if not arvore.existeRotuloAresta(a):
                    if not arvore.existeVertice(r):
                        arvore.adicionaVertice(r)
                    if not arvore.existeVertice(vertice):
                        arvore.adicionaVertice(vertice)
                        arvore.adicionaAresta(a, r, vertice)
                    else:
                        return True
        return False'''

    def ha_ciclo2(self, arvore, r):
            arestas_na_raiz = self.arestas_sobre_vertice(r)
            for a in arestas_na_raiz:
                if self.eh_laco(a):
                    return True
                vertice = self.vertice_oposto(a, r)
                if not arvore.existeRotuloAresta(a):
                    if not arvore.existeVertice(r):
                        arvore.adicionaVertice(r)
                    if arvore.existeVertice(vertice):
                        return True
                    else:
                        arvore.adicionaVertice(vertice)
                        arvore.adicionaAresta(a, r, vertice)
                        if self.ha_ciclo2(arvore, vertice):
                            return True
            return False

    def eh_desconexo(self):
        if len(self.A) < len(self.N) - 1:
            return True
        return False

    def arestas_no_grafo(self, arvore):
        arestas = self.A
        arestas_arvore = arvore.A
        for a in arestas_arvore:
            try:
                if arestas[a] != arestas_arvore[a]:
                    return False
            except KeyError:
                return False
        return True

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass
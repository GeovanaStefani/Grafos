from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *
import colorama
from colorama import Fore
from colorama import Style

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def indice(self, V=''):
        if V not in self.N:
            raise VerticeInvalidoException("Vertíce Inválido!")
        return self.N.index(V)

    def vertice(self, I=''):
        if I == '' or I>=len(self.N):
            raise VerticeInvalidoException("Indice Inválido!")
        return self.N[I]

    def monta_aresta(self, v1, v2):
        '''Monta uma string com os 2 vértices passados.

        :param v1: Vértice 1
        :param v2: Vértice 2
        :return: 'V1-V2'
        '''
        return v1 + "-" + v2

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        v_nao_adjacentes = set()
        for il, linha in enumerate(self.M):
            for ic, coluna in enumerate(linha):
                if il <= ic and il != ic and len(coluna) == 0:
                    v1 = self.vertice(il)
                    v2 = self.vertice(ic)
                    aresta = self.monta_aresta(v1, v2)
                    v_nao_adjacentes.add(aresta)
        return v_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        for il, linha in enumerate(self.M):
            for ic, coluna in enumerate(linha):
                if il == ic and len(coluna)>0:
                    return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        grau = 0
        i = self.indice(V)
        for il, linha in enumerate(self.M):
            for ic, coluna in enumerate(linha):
                if il <= ic and (il == i or ic == i) and len(coluna)>0:
                    peso = 1
                    if il == ic:
                        peso = 2
                    grau += peso * len(coluna)
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for il, linha in enumerate(self.M):
            for ic, coluna in enumerate(linha):
                if il <= ic:
                    if len(coluna)>1:
                        return True
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        arestas_v = set()
        i = self.indice(V)
        for il, linha in enumerate(self.M):
            for ic, coluna in enumerate(linha):
                if il <= ic and (il == i or ic == i) and len(coluna) > 0:
                    for aresta in coluna:
                        arestas_v.add(aresta)
        return arestas_v

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

    def nocao_matriz(self):
        print(end='  ')
        for elem in self.N:
            print(f' {elem}', end='')
        print()
        for i, posicao in enumerate(self.M):
            print(f'{self.N[i]}: ', end='')
            for c, elem in enumerate(posicao):
                qntd_a = len(elem)
                if i<=c:
                    if qntd_a == 0:
                        print(Fore.MAGENTA + str(qntd_a) + Style.RESET_ALL, end=' ')
                    else:
                        print(Fore.LIGHTBLUE_EX + str(qntd_a) + Style.RESET_ALL, end=' ')
                else:
                    print(Fore.RED + str(qntd_a) + Style.RESET_ALL, end=' ')
            print()
        print()
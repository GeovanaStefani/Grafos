import unittest
from meu_grafo import *
#from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Um laço com um não laço não é uma paralela
        self.g = MeuGrafo(['C', 'E'])
        self.g.adicionaAresta('a1', 'C', 'C')
        self.g.adicionaAresta('a2', 'C', 'E')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C')
        self.g_p4.adicionaAresta('a2', 'J', 'E')
        self.g_p4.adicionaAresta('a3', 'C', 'E')
        self.g_p4.adicionaAresta('a4', 'P', 'C')
        self.g_p4.adicionaAresta('a5', 'P', 'C')
        self.g_p4.adicionaAresta('a6', 'T', 'C')
        self.g_p4.adicionaAresta('a7', 'M', 'C')
        self.g_p4.adicionaAresta('a8', 'M', 'T')
        self.g_p4.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

        self.grafo_atv = MeuGrafo(list('ABCDEFGHIJK'))

        self.grafo_atv.adicionaAresta('a1', 'A', 'B')
        self.grafo_atv.adicionaAresta('a2', 'B', 'C')
        self.grafo_atv.adicionaAresta('a3', 'C', 'D')
        self.grafo_atv.adicionaAresta('a4', 'D', 'E')
        self.grafo_atv.adicionaAresta('a5', 'E', 'B')
        self.grafo_atv.adicionaAresta('a6', 'B', 'F')
        self.grafo_atv.adicionaAresta('a7', 'F', 'H')
        self.grafo_atv.adicionaAresta('a8', 'H', 'G')
        self.grafo_atv.adicionaAresta('a9', 'G', 'B')
        self.grafo_atv.adicionaAresta('a10', 'G', 'A')
        self.grafo_atv.adicionaAresta('a11', 'G', 'K')
        self.grafo_atv.adicionaAresta('a12', 'G', 'J')
        self.grafo_atv.adicionaAresta('a13', 'G', 'I')
        self.grafo_atv.adicionaAresta('a14', 'A', 'J')
        self.grafo_atv.adicionaAresta('a15', 'J', 'K')
        self.grafo_atv.adicionaAresta('a16', 'J', 'I')
        self.grafo_atv.adicionaAresta('a17', 'B', 'D')

        self.grafo_sem_ciclo = MeuGrafo(list('ABCDEFGHIJK'))
        self.grafo_sem_ciclo.adicionaAresta('a1', 'A', 'J')
        self.grafo_sem_ciclo.adicionaAresta('a2', 'A', 'G')
        self.grafo_sem_ciclo.adicionaAresta('a3', 'A', 'B')
        self.grafo_sem_ciclo.adicionaAresta('a4', 'J', 'K')
        self.grafo_sem_ciclo.adicionaAresta('a5', 'J', 'I')
        self.grafo_sem_ciclo.adicionaAresta('a6', 'G', 'H')
        self.grafo_sem_ciclo.adicionaAresta('a7', 'B', 'F')
        self.grafo_sem_ciclo.adicionaAresta('a8', 'B', 'C')
        self.grafo_sem_ciclo.adicionaAresta('a9', 'B', 'D')
        self.grafo_sem_ciclo.adicionaAresta('a10', 'B', 'E')

        self.g_p_sem_ciclo = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_ciclo.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_ciclo.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_ciclo.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_ciclo.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_ciclo.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_ciclo.adicionaAresta('a7', 'T', 'Z')

        self.g_p_d = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_d.adicionaAresta('a1', 'J', 'C')
        self.g_p_d.adicionaAresta('a3', 'P', 'C')
        self.g_p_d.adicionaAresta('a4', 'T', 'C')
        self.g_p_d.adicionaAresta('a5', 'M', 'C')
        self.g_p_d.adicionaAresta('a7', 'T', 'Z')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertFalse(self.g.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def teste_busca(self):
        graphList = [self.g_p, self.g_c, self.g_l5, self.g_p_sem_paralelas, self.grafo_atv, self.g_p_sem_ciclo,
                     self.grafo_sem_ciclo]

        for grafos in graphList:
            for i in grafos.N:
                arvore_dfs = grafos.dfs(i)
                self.assertTrue(
                    grafos.arestas_no_grafo(arvore_dfs) and
                    not arvore_dfs.ha_ciclo() and
                    len(arvore_dfs.N) == len(grafos.N)
                    #not arvore_dfs.conexo()
                )
                arvore_bfs = grafos.bfs(i)
                self.assertTrue(
                    grafos.arestas_no_grafo(arvore_bfs) and
                    not arvore_bfs.ha_ciclo() and
                    len(arvore_bfs.N) == len(grafos.N)
                    #not arvore_bfs.conexo()
                )

    def teste_caminho_true(self):
        graphList = [(self.g_p, 8), (self.g_c, 5), (self.g_l5, 2), (self.g_p_sem_paralelas, 5),
                     (self.grafo_atv, 17), (self.g_p_sem_ciclo, 3), (self.grafo_sem_ciclo, 4)]

        for grafo in graphList:
            g = grafo[0]
            c_max = grafo[1]

            for i in range(0, c_max+1):
                caminho_i = g.caminho(i)
                self.assertTrue(g.caminho_no_grafo(caminho_i))
                self.assertTrue((len(caminho_i)-1)/2 == i)

    def teste_caminho_false(self):
        graphList = [(self.g_p, 8), (self.g_c, 5), (self.g_l5, 2), (self.g_p_sem_paralelas, 5),
                     (self.grafo_atv, 17), (self.g_p_sem_ciclo, 3), (self.grafo_sem_ciclo, 4)]

        for grafo in graphList:
            g = grafo[0]
            c_excede= grafo[1]+1

            self.assertFalse(g.caminho(c_excede))

    def teste_ciclo_true(self):
        graphList = [self.g_p, self.g_c, self.g_l5, self.g_p_sem_paralelas, self.grafo_atv]

        for grafo in graphList:
            ciclo = grafo.ha_ciclo()
            self.assertTrue(grafo.caminho_no_grafo(ciclo))
            self.assertTrue(ciclo[0] == ciclo[-1])

    def teste_ciclo_false(self):
        graphList = [self.g_p_sem_ciclo, self.grafo_sem_ciclo]

        for grafo in graphList:
            self.assertFalse(grafo.ha_ciclo())

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p2.conexo())
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_d2.conexo())

    def teste_arestas_no_grafo(self):
        graphs = [self.g_p, self.g_c, self.g_l5, self.g_p_sem_paralelas, self.grafo_atv]

        for grafo in graphs:
            for r in grafo.N:
                arvoreDFS = grafo.dfs(r)
                arvoreBFS = grafo.bfs(r)
                self.assertTrue(grafo.arestas_no_grafo(arvoreDFS))
                self.assertTrue(grafo.arestas_no_grafo(arvoreBFS))
                self.assertFalse(arvoreDFS.arestas_no_grafo(grafo))
                self.assertFalse(arvoreBFS.arestas_no_grafo(grafo))
    def teste_dijkstra(self):
        self.assertEqual(self.g_p.dijkstra('J', 'Z'), ['Z-T', 'T-C', 'C-J'])
        self.assertEqual(self.g_p.dijkstra('P', 'Z'), ['Z-T', 'T-C', 'C-P'])
        self.assertEqual(self.g_p.dijkstra('P', 'M'), ['M-C', 'C-P'])
        self.assertEqual(self.grafo_atv.dijkstra('I', 'E'), ['E-B', 'B-G', 'G-I'])
        self.assertEqual(self.grafo_atv.dijkstra('C', 'J'), ['J-A', 'A-B', 'B-C'])
        self.assertEqual(self.grafo_atv.dijkstra('I', 'A'), ['A-G', 'G-I'])

        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(print(self.g_p.dijkstra('j', 'Z')), ['Z-T', 'T-C', 'C-J'])
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(print(self.grafo_atv.dijkstra('I', 'e'), ['E-B', 'B-G', 'G-I']))



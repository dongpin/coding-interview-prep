from collections import OrderedDict

from python.basic_algorithm.graph import Graph, bfs, dfs, dfs_iterative, topological_sort


def test_create_graph():
    g = Graph()
    g.add_edge(0, 1)
    g.add_vertex(2)
    g.add_edge(2, 1)
    assert g.graph[2] == [1]
    assert g.graph.get(1) is None


test_graph1 = {'A': ['B', 'C'],
               'B': ['E', 'F', 'G'],
               'C': ['E', 'G', 'K'],
               'K': ['I', 'J'],
               'J': ['A'],
               'Z': []}

test_graph2 = OrderedDict()
test_graph2['A'] = []
test_graph2['B'] = []
test_graph2['C'] = []

test_graph3 = {'A': ['B', 'C']}
test_graph4 = {}


def test_dfs():
    assert dfs(test_graph1) == ['A', 'B', 'E', 'F', 'G', 'C', 'K', 'I', 'J', 'Z']
    assert dfs(test_graph2) == ['A', 'B', 'C']
    assert dfs(test_graph3) == ['A', 'B', 'C']
    assert dfs(test_graph4) == []


def test_dfs_iterative():
    assert dfs_iterative(test_graph1) == ['A', 'B', 'E', 'F', 'G', 'C', 'K', 'I', 'J', 'Z']
    assert dfs_iterative(test_graph2) == ['A', 'B', 'C']
    assert dfs_iterative(test_graph3) == ['A', 'B', 'C']
    assert dfs_iterative(test_graph4) == []


def test_bfs():
    assert bfs(test_graph1) == ['A', 'B', 'C', 'E', 'F', 'G', 'K', 'I', 'J', 'Z']
    assert bfs(test_graph2) == ['A', 'B', 'C']
    assert bfs(test_graph3) == ['A', 'B', 'C']
    assert bfs(test_graph4) == []


test_graph5 = {'A': ['C'],
               'B': ['C', 'D'],
               'C': ['E'],
               'D': ['F'],
               'E': ['H', 'F'],
               'F': ['G'],
               'G': [],
               'H': []}


def test_topological_sort():
    assert topological_sort(test_graph5) == ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']

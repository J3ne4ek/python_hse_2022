import ast
import os
import networkx as nx
from easy import get_fib
import inspect
import matplotlib.pyplot as plt

def visit(node, graph: nx.DiGraph):
    name = str(type(node).__name__)
    graph.add_node(name)
    for child in ast.iter_child_nodes(node):
        graph.add_edge(name, visit(child, graph))
    return name   
    
def create(sourse):
    graph = nx.DiGraph()
    visit(ast.parse(sourse), graph)
    plt.figure(figsize=(10, 10), dpi=150)
    subax1 = plt.subplot()
    options = {
        'node_color': 'blue',
        'node_size': 300,
        'width': 1,
        'arrowsize': 5,
    }
    nx.draw_networkx(graph, arrows=True, **options)
    plt.show()
    plt.savefig('artifacts/ast.png')
    
if __name__ == '__main__':
    create(inspect.getsource(get_fib))
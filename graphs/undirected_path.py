from typing import Dict

from edges import edge_list
from builders import build_graph

graph = build_graph(edge_list)


def undirected_has_path(*, graph:Dict, source:str, destination:str, visited:dict) -> bool:
    if source == destination: return True
    if visited.get(source): return False
    visited.update({source: True})
    
    neighbours = graph.get(source)
    for neighbour in neighbours:
        if undirected_has_path(graph=graph, source=neighbour, destination=destination, visited=visited):
            return True
    
    return False

if __name__ == '__main__':
    print(undirected_has_path(graph=graph, source='i', destination='k', visited={}))

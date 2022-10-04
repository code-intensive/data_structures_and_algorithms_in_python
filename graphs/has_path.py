from typing import Dict

from graphs import graph


def has_path(*, graph:Dict, source:str, destination:str) -> bool:
    if source == destination:
        return True
    
    neighbours = graph.get(source)
    for neighbour in neighbours:
        if has_path(graph=graph, source=neighbour, destination=destination):
            return True
    
    return False

if __name__ == '__main__':
    print(has_path(graph=graph, source='c', destination='e'))
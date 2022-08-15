from typing import Dict


def has_path(*, graph:Dict, source:str, destination:str) -> bool:
    if source == destination:
        return True
    
    neighbours = graph.get(source)
    for neighbour in neighbours:
        if has_path(graph=graph, source=neighbour, destination=destination):
            return True
    
    return False


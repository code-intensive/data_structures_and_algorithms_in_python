from typing import Dict, List

from graphs import graph


def breadth_first_search(graph:dict, source:str):
    queue = [source]
    del source
    
    while len(queue) > 0:
        current = queue.pop()
        neighbours = graph.get(current)
        
        print(current)
        
        for neighbour in neighbours:
            queue.insert(0, neighbour)
            
breadth_first_search(graph, 'a')

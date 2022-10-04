from typing import Any, Dict

from graphs import multi_component_graph


def explore(graph:Dict, node:Any, visited:set) ->bool:
    if node in visited:
        return False
    
    visited.add(node)
    
    for neighbour in graph[node]:
        explore(graph, neighbour, visited)
        
    return True

def component_count(graph:Dict[Any, Any]) -> int:
    visited = set()
    count = 0
    
    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1
    return count

if __name__ == '__main__':
    print(component_count(multi_component_graph))

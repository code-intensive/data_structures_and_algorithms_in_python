from typing import Any, Dict

from graphs import graph


def count_nodes(graph:Dict, node:Any, visited:set, count) ->bool:
    if node in visited: return False
    
    visited.add(node)
    count += 1
    
    for neighbour in graph[node]:
        count_nodes(graph, neighbour, visited, count)
        
    return count

def component_count(graph:Dict[Any, Any]) -> int:
    visited = set()
    max_count = 0
    
    for node in graph:
        counter = 0
        count = count_nodes(graph, node, visited, counter)
        if count is False: continue
        max_count = max(max_count, count)
    return max_count

if __name__ == '__main__':
    print(component_count(graph))

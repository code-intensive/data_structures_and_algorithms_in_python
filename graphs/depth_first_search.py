from typing import Dict, List

from graphs import graph


def depth_first_search(graph:Dict, source:str) -> List:
    stack = [source]
    del source
    
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        
        for neighbour in graph[current]:
            stack.append(neighbour)

if __name__ == '__main__':
    print(depth_first_search(graph, 'a'))

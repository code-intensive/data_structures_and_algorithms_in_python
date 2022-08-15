from typing import List, Dict


def build_graph(edge_list: List[List]) -> Dict:
    graph: dict = {}

    for edge_pair in edge_list:
        edge_1, edge_2 = edge_pair
        
        graph[edge_1] = graph.get(edge_1, [])
        graph[edge_2] = graph.get(edge_2, [])
        
        graph[edge_1].append(edge_2)
        graph[edge_2].append(edge_1)
        
    return graph

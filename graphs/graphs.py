from typing import Dict, List


graph: Dict[str, List] = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

multi_component_graph: Dict[str, List] = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['a'],
    'e': ['d'],
    'f': [],
    'h': [],
    'i': ['j'],
    'j': ['i']
}

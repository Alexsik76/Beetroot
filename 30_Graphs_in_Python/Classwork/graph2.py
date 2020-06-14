from collections import deque


def breadth_first_search(graph, root, target): 
    visited, queue = set(), deque([root])
    while queue: 
        vertex = queue.popleft()
        yield vertex
        visited.add(vertex)
        if target in graph[vertex]:
            yield target
            found = True
            break 
        if vertex in graph.keys():
            queue.extend(n for n in graph[vertex] if n not in visited)
    if not found:
        print( "So sorry, but a connecting path doesn't exist :(")   

if __name__ == '__main__':
    graph = {
    'Math-151': ['CS-220'],
    'CS-220': ['CS-360', 'CS-477'],
    'CS-360': ['CS-490'],
    'CS-477': ['CS-490'],
    'CS-150': ['CS-220', 'CS-151'],
    'CS-151': ['CS-250', 'CS-230'],
    'CS-230': ['CS-466']
}

    path = list(breadth_first_search(graph, 'Math-151', 'CS-490'))
    print(*path, sep= ' --> ')

from queue import deque

graph = {
    'Math-151': ['CS-220'],
    'CS-220': ['CS-360', 'CS-477'],
    'CS-360': ['CS-490'],
    'CS-477': ['CS-490'],
    'CS-150': ['CS-220', 'CS-151'],
    'CS-151': ['CS-250', 'CS-230'],
    'CS-230': ['CS-466']
}


def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.appendleft((next, path+[next]))
                # print(*queue)

print(list(bfs_paths(graph, 'Math-151', 'CS-490')))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print(*list(shortest_path(graph, 'Math-151', 'CS-490')), sep= ' --> ')

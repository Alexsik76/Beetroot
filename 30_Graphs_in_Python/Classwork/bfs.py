# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = set()
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                print(queue)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.add(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 
# sample graph implemented as a dictionary
graph ={
    'Math-151': ['CS-220'],
    'CS-220': ['CS-360', 'CS-477', 'CS-151'],
    'CS-360': ['CS-490', 'CS-466'],
    'CS-477': ['CS-490'],
    'CS-150': ['CS-220', 'CS-151', 'CS-250'],
    'CS-151': ['CS-250', 'CS-230', 'CS-360'],
    'CS-230': ['CS-466'],
    'CS-490': ['CS-230'], 
    'CS-466': ['CS-360']
}
path = bfs_shortest_path(graph, 'Math-151', 'CS-250')  # returns ['G', 'C', 'A', 'B', 'D']
print(path)
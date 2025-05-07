from multiprocessing import Pool, cpu_count
from grafo import grafo  # Import your graph here
from time import perf_counter
from collections import deque

def dfs_iterative(graph, start, visited, component):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            stack.extend(graph.get(node, []))

def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs_iterative(graph, node, visited, component)
            components.append(component)

    return components

def bfs_batch_subgraph(args):
    graph, subcomponents = args
    local_visited = []

    for component in subcomponents:
        queue = deque([component[0]])  # Entry point
        visited = set()

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(f"[{component[0]}] Visiting: {vertex}")
                visited.add(vertex)
                local_visited.append(vertex)
                for neighbor in graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
    
    return local_visited

def group_components(components, num_groups):
    # Group components into approximately balanced blocks
    sorted_components = sorted(components, key=len, reverse=True)
    groups = [[] for _ in range(num_groups)]
    weights = [0] * num_groups

    for comp in sorted_components:
        smallest_group = weights.index(min(weights))
        groups[smallest_group].append(comp)
        weights[smallest_group] += len(comp)

    return groups

def bfs(graph, number_of_workers=cpu_count()):
    start = perf_counter()

    components = find_connected_components(graph)
    groups = group_components(components, number_of_workers)
    args = [(graph, group) for group in groups]

    with Pool(processes=number_of_workers) as pool:
        results = pool.map(bfs_batch_subgraph, args)

    # Merge results
    visited = set()
    for partial in results:
        visited.update(partial)

    end = perf_counter()

    print(f"\nTotal visited nodes: {len(visited)}")
    print(f"Execution time: {end - start:.6f} seconds")

if __name__ == "__main__":
    bfs(grafo, number_of_workers=4)  # Adjust number of processes as needed

import heapq
def dijkstra(graph, start, end):
    pq, distances, predecessors = [(0, start)], {node: float('inf') for node in graph}, {node: None for node in graph}
    distances[start] = 0
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == end:
            break
        for neighbor, travel_time in graph[current_node]:
            if (distance := current_distance + travel_time) < distances[neighbor]:
                distances[neighbor], predecessors[neighbor] = distance, current_node
                heapq.heappush(pq, (distance, neighbor))
    path, node = [], end
    while node:
        path.append(node)
        node = predecessors[node]
    return distances[end], path[::-1]
graph = {input("Enter location: "): [] for _ in range(int(input("Enter number of nodes: ")))}
for _ in range(int(input("Enter number of paths: "))):
    start, end, time = input("Enter path (from to time): ").split()
    graph[start].append((end, int(time)))

start, end = input("Enter start location: "), input("Enter destination: ")
travel_time, route = dijkstra(graph, start, end)
print(f"Shortest travel time from {start} to {end} is {travel_time}")
print(f"The shortest path is: {' -> '.join(route)}")
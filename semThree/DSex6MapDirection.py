def get_directions(start, end):
    # Define the graph as a dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Simple BFS to find the path
    visited = []
    queue = [[start]]
    
    if start == end:
        return f"You are already at {start}."
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == end:
                    return f"Directions: {' -> '.join(new_path)}"
            visited.append(node)
    
    return "No path found."
if __name__=="__main__":
    start_location = input("Enter your current location: ")
    end_location = input("Enter your destination: ")
    print(get_directions(start_location, end_location))
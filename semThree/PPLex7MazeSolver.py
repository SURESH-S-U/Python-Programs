def maze_solver(maze, start, end):
    stack = [start]  # Stack to store the current path
    visited = []     # List to store visited cells

    while stack:
        position = stack.pop()
        
        # If we've reached the end point, return the path
        if position == end:
            visited.append(end)
            return visited
        
        if position not in visited:
            visited.append(position)
            
            # Explore neighbors in 4 directions: up, down, left, right
            x, y = position
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                # Check bounds and if cell is open
                if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and 
                    maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
                    stack.append((new_x, new_y))
    
    # Return None if no path is found
    return None


# Function to take user input for the maze
def get_user_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    print("Enter the maze (0 for open space, 1 for walls):")
    maze = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        maze.append(row)

    return maze


# Example usage with default start and end points
maze = get_user_input()

# Set default starting and ending points
start = (0, 0)  # Top-left corner
end = (len(maze) - 1, len(maze[0]) - 1)  # Bottom-right corner

path = maze_solver(maze, start, end)

if path:
    print("Path found:", path)
else:
    print("No path found.")

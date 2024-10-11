def dirReduc(arr):
    # Dictionary to easily look up opposites
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    
    # Stack to keep track of the valid path
    path = []
    
    # to Iterate through each direction in the input list
    for direction in arr:
        # If the path is not empty and the last direction in the path cancels out the current one
        if path and opposites[direction] == path[-1]:
            # Remove the last direction from the path since it cancels out with the current one
            path.pop()
        else:
            # add the current direction to the path
            path.append(direction)
    
    # Return path
    return path


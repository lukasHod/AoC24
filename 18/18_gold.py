import heapq
import copy

from collections import defaultdict

#file, mapSize = open(__file__ + '\\..\\testInput.txt', 'r'), 7
file, mapSize = open(__file__ + '\\..\\input.txt', 'r'), 71

def printArray(arr):
    print('\n\n')
    for row in arr:
        rs = map(str, row)
        print(''.join(rs))


def dijkstra_all_shortest_paths(maze, start, goal):
    directions = {'r': (0, 1), 'd':(1, 0), 'l': (0, -1), 'u': (-1, 0)}  # Right, Down, Left, Up
    rows, cols = len(maze), len(maze[0])
    # Priority queue: (distance, (x, y))
    pq = [(0, start)]
    distances = {start: 0}
    paths = defaultdict(list)
    paths[start] = [[start]]  # Store all paths to each node
    
    while pq:
        current_dist, (x, y) = heapq.heappop(pq)
        # If we reach the goal, we're done
        if (x, y) == goal:
            print('found')
            print(current_dist)
            return paths[goal]

        # Explore neighbors
        for d in directions:
            dx, dy = directions[d][0], directions[d][1]
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or maze[nx][ny] == '#':
                continue

            new_dist = current_dist + 1
            neighbor = (nx, ny)
            
            # If a shorter path is found, update distance and reset paths
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                paths[neighbor] = [path + [neighbor] for path in paths[(x, y)]]
                heapq.heappush(pq, (new_dist, neighbor))

    return []  # No path found




inputMap = []
for i in range(mapSize):
    inside = []
    for j in range(mapSize):
        inside.append('.')
    inputMap.append(inside)

for i, line in enumerate(file.readlines()):
    line = line.removesuffix('\n')
    cords = line.split(',')
    inputMap[int(cords[1])][int(cords[0])] = '#'
    
    if i == 2907:
        print(cords)
        break


originMap = copy.deepcopy(inputMap)

paths = dijkstra_all_shortest_paths(inputMap,(0, 0), (mapSize-1, mapSize-1))


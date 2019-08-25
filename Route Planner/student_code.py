import math
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# Resource Used - http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html

def heuristic(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def path(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path


def shortest_path(M, start, goal):
    
    explore = PriorityQueue()
    explore.put(start, 0)
    
    previous = {start: None}
    g = {start: 0}

    while not explore.empty():
        current = explore.get()

        if current == goal:
            path(previous, start, goal)

        for n in M.roads[current]:
            tempscore = g[current] + heuristic(M.intersections[current], M.intersections[n])
            
            if n not in g or tempscore < g[n]:
                g[n] = tempscore
                tscore = tempscore + heuristic(M.intersections[current], M.intersections[n])
                explore.put(n, tscore)
                previous[n] = current

    return path(previous, start, goal)


import math
import heapq
def euclidean_dis(M, node1, node2):
    point1 = M.intersections[node1]
    point2 = M.intersections[node2]
    return math.sqrt(pow(point1[0] - point2[0],2) + pow(point2[1] - point2[1],2))

#For this implementation euclidean distance was used as the heuristic function but another metric the manhattan distance can also be used as the heuristic funcion. Defined below.
def manhattan_dis(M, node1, node2):
    point1 = M.intersections[node1]
    point2 = M.intersections[node2]
    return (abs(point1[0] - point2[0]) + abs(point2[1] - point2[1]))


def shortest_path(M,start,goal):
    if start == goal:
        return [start]
    
    frontier = []
    heapq.heappush(frontier, (0, start))
    visited = {start: {'f' : 0, 'g': 0, 'h': euclidean_dis(M, start, goal), 'parent':None}}
    path = []
    while len(frontier):
        #node = frontier.pop(0)
        node = heapq.heappop(frontier)
        if node[1] == goal:
            node = node[1]
            break
        else:
            children = M.roads[node[1]]
            for child in children:
                distance = euclidean_dis(M, child, node[1])
                heuristic = euclidean_dis(M, child, goal)
                if child in visited and visited[child]['f'] > distance+node[0]+heuristic:
                    visited[child] ={'f' :distance+node[0]+heuristic, 'g': distance+node[0], 'h' : heuristic ,'parent' : node[1]}
                    frontier = [tup for tup in frontier if tup[1] != child]
                    heapq.heapify(frontier)
                    #frontier.append([child, distance+node[0]+heuristic])
                    heapq.heappush(frontier,(distance+node[0]+heuristic, child))
                if child not in visited:
                    visited[child] ={'f' :distance+node[0]+heuristic, 'g': distance+node[0], 'h' : heuristic ,'parent' : node[1]}
                    #frontier.append([child, distance+node[0]+heuristic])
                    heapq.heappush(frontier,(distance+node[0]+heuristic, child))
                    
        #frontier.sort(key = lambda x: x[1])

    while node is not None:
        path.append(node)
        node = visited[node]['parent']
    path.reverse()

    print("shortest path called")
    print(path)
    return path

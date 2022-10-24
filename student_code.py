import math
import heapq

#For this implementation euclidean distance was used as the heuristic function but another metric the manhattan distance can also be used as the heuristic funcion. Defined below. Euclidean distance metric is an admissible and consistent metric which means it is an optimistic "estimate" of the distance and will never overestimate the distance between two points and the direct distance between two points is always less than equal to the distance between those points through a third point. The euclidean distance is the shortest distance i.e. a straight line (only true for euclidean geometry). Manhattan distance can be used as a heuristic but it is not the shortest distance for this application. As the name suggests it is distance computed in a city designed like Manhattan where everything is in a grid. So distance between two points would be summation of absolute values of traversal through all the points from start to goal location and not a straight line distance. For this application manhattan distance is admissible and consistent but does not estimate the shortest path. Note Manhattan distance as described above is based on the assumption that we can only move up down left or right on a grid. If diagonal motion is allowed on a grid between two adjacent points then diagonal distance can be added. In terms of path lengths euclidean will give the shortest then the manhattan distance metric with diagonal movement and the last will be manhattan distance original. Note this all assumes we are in euclidean space. Now if we move to an application where we are no longer in euclidean space but say a spherical surface then we need to bring into consideration other dimensions apart from the x,y,z. For the spherical space angular distance will have to be added to the metric distance and the notion of admissibility and consistency becomes a bit complicated.  Other metrics which can be considered are the infinity distance metric also known has max norm and the p-norm but these are not really of much use in the application we have here. Point to note p-norm is the generalization of euclidean distance metric.

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
            #For this implementation euclidean distance was used as the heuristic function but another metric the manhattan distance can also be used as the heuristic funcion. Defined below.
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

"""
#Search Algorithms - Uninformed
Author: Sebastian C.
"""

from collections import namedtuple,deque
city = {
    's':{
        'a':7,
        'b':2,
        'c':3
    },
    'a':{
        's':7,
        'b':3,
        'd':4
    },
    'b':{
        's':2,
        'a':3,
        'd':4,
        'h':1
    },
    'c':{
        'l':2,
        's':3
    },
    'd':{
        'a':4,
        'b':4,
        'f':5
    },
    'f':{
        'h':3,
        'd':5
    },
    'h':{
        'g':2,
        'b':1,
        'f':3
    },
    'g':{
        'h':2,
        'e':2
    },
    'l':{
        'i':4,
        'j':6,
        'c':2
    },
    'i':{
        'l':4,
        'j':6,
        'k':4
    },
    'j':{
        'l':6,
        'i':6,
        'k':4
    },
    'k':{
        'e':5,
        'i':4,
        'j':4
    },
    'e':{
        'g':2,
        'k':5
    }

}

heuristic = {
    's' : 10,
    'a' : 9,
    'b' : 7,
    'c' : 8,
    'd' : 8,
    'l': 6,
    'i' : 4,
    'j' : 4,
    'k' : 3,
    'g' : 3,
    'h' : 6,
    'f' : 6,
    'e':  0
}

"""##Functions for BFS and DFS


"""

def bfs(start, end):
    '''
    Breadth first search algorithm to find the shortest route 
    between cities.
    '''
    visited = {c:0 for c in city.keys()}
    pclist = {}
    queue = deque()
    queue.append(start)
    while len(queue) != 0:
        front = queue.popleft()
        if front == end:
            return pclist
        neighbors = [i for i in city[front].keys()]
        for neighbor in neighbors:
            if visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = 1
                pclist[neighbor] = front
    return []


def path(pclist,start,end):
    '''
    Finds the actual path given a list of points 
    and their parents 
    '''
    if pclist == []:
        return "No path found"
    count = end
    path = []
    path.insert(0,count)
    while count != start:
        count  = pclist[count]
        path.insert(0,count)
    return path

x  = bfs('s','e')
print(path(x,'s','e'))


def dfs(start, end):
    '''
    Depth first search algorithm to find the shortest route 
    between cities. Could use recursion but decided to use
    an iterative apprach 
    '''
    visited = {c:0 for c in city.keys()}
    pclist = {}
    stack = []
    stack.append(start)
    while len(stack) != 0:
        front = stack.pop()
        if visited[front] == 0:
            visited[front] = 1
            if front == end:
                return pclist
            else:
                neighbors = [i for i in city[front].keys()]
                for neighbor in neighbors:
                    if visited[neighbor] == 0:
                        stack.append(neighbor)
                        pclist[neighbor] = front
    return [] 

y = dfs('s','e')
print(path(y,'s','e'))


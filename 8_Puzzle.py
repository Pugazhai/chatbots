import copy
from heapq import heappush, heappop

n = 3
rows = [1, 0, -1, 0]
cols = [0, -1, 0, 1]


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not bool(self.heap)


class Node:
    def __init__(self, parent, matrix, empty_tile_pos, cost, level):
        self.parent = parent
        self.matrix = matrix
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, other):
        return self.cost < other.cost


def CalculateCost(matrix, final):
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] and matrix[i][j] != final[i][j]:
                count += 1
    return count


def NewNode(matrix, empty_tile_pos, new_empty_tile_pos, level, parent, final):
    new_matrix = copy.deepcopy(matrix)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    cost = CalculateCost(new_matrix, final)
    return Node(parent, new_matrix, new_empty_tile_pos, cost, level)


def PrintMatrix(matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


def IsSafe(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def PrintPath(root):
    if root is None:
        return
    PrintPath(root.parent)
    PrintMatrix(root.matrix)
    print()


def Solve(initial, empty_tile_pos, final):
    pq = PriorityQueue()
    cost = CalculateCost(initial, final)
    root = Node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)
    while not pq.empty():
        minimum = pq.pop()
        if minimum.cost == 0:
            PrintPath(minimum)
            return
        for i in range(4):
            new_tile_pos = [minimum.empty_tile_pos[0] + rows[i], minimum.empty_tile_pos[1] + cols[i]]
            if IsSafe(new_tile_pos[0], new_tile_pos[1]):
                child = NewNode(minimum.matrix, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final)
                pq.push(child)


initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_tile_pos = [1, 2]
Solve(initial, empty_tile_pos, final)

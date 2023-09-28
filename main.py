# Author: TaeKil Oh
# Initial Date: SEP 27TH, 2023
# Submission Date: OCT 5TH, 2023
# File Name:
# Purpose: Mile-Stone1 of Artificial Intelligence FQ23 CS5610 Quarter Project

"""
The purpose based on the given matrix,
read and return the type(emotion)

Construct a tree from a matrix by performing a BFS traversal.

the matrices are provided as .txt files and in 0 and 1.
0 is white in grid
1 is black in grid

my questions are,
    1) location and direction matter?
        for example, the smile is at the bottom side from the center,
        but, it will be located at the top.

    2) in addition to that, the direction of smile being vertical, not horizontal

    3) furthermore, Do I need to care about multiple smile?

    4) so, How can I figure it out that the problem multiple smile?
"""

# Create 8 X 8 2D-array to test BFS
# Create an array of c columns and r rows
# This is the test matrix
c = 8
r = 8
arr = [[0] * c for i in range(r)]

# loop for the length of the outer list
for i in range(r):
    # loop for the length of the inner list
    for j in range(c):
        arr[i][j] = i*c + j + 1

for row in arr:
    print(row)

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)

class Queue:
    def __init__(self):
        self.items = []

    def get_item(self):
        return self.items[0]

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

# Identify the neighbors of a cell in a 2-D grid
def get_neighbor_coordinates(matrix, row, col):
    neighbors_coordinates = []
    # define relative directions(North, South, West, East)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for directionRow, directionColumn  in directions:
        newRow, newCol = row + directionRow, col + directionColumn
        # check the new position is within boundary of the grid
        # if less than 0 or greater than length of grid -> out of boundary
        # the combination should be "and"
        if 0<= newRow < len(matrix) and 0 <= newCol <len(matrix[0]):
            neighbors_coordinates.append((newRow,newCol))
    return neighbors_coordinates

def matrix_to_tree(matrix):
    # Start from the cell with coordinates (0, 0)
    root = Node(0,0)
    queue = Queue()
    queue.enqueue(root)
    visited = set()

    while not queue.is_empty():

        current_node = queue.get_item()
        if current_node is None:
            continue

        visited.add((current_node.row, current_node.col))
        for neighbor_row, neighbor_col in get_neighbor_coordinates(matrix, current_node.row, current_node.col):
            if (neighbor_row, neighbor_col) not in visited:
                new_node = Node(neighbor_row, neighbor_col)
                current_node.add_neighbor(new_node)
                queue.enqueue(new_node)
                visited.add((neighbor_row, neighbor_col))
        queue.dequeue()
    return root

def print_tree(arr, node, level=0, prefix='Root: '):
    if node is not None:
        if level == 0:
            print(prefix + str(arr[node.row][node.col]))
        else:
            indent = ' ' * (level - 1) * 4
            print(f'{indent}{" " * 2 * (level - 1)}|-- {str(arr[node.row][node.col])}')
        for i, neighbor in enumerate(node.neighbors):
            is_last = i == len(node.neighbors) - 1
            print_tree(arr, neighbor, level + 1, prefix=' ' * 2 * (level - 1) + '|-- ' if not is_last else ' ' * 2 * (level - 1) + '     ')

root = matrix_to_tree(arr)
# Print the tree starting from the root node
print_tree(arr, root)










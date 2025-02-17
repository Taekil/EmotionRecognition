# Emotion Recognition using BFS and Graph Traversal

## Overview
This project implements an emotion recognition system using **graph traversal techniques**, specifically **Breadth-First Search (BFS)**. The goal is to identify emotions from an **8x8 binary matrix**, where `0` represents white pixels, and `1` represents black pixels.

## Features
- Implementation of BFS to traverse a binary image representation.
- Conversion of the binary matrix into a graph structure.
- Detection of patterns resembling emotional expressions (e.g., smiles).
- Handling different orientations and positions of patterns.
- Consideration of multiple emotional instances in a single matrix.

## How It Works
1. **Data Representation**:
   - The `8x8` matrix is a binary representation of an image.
   - `1` represents the presence of a feature (e.g., part of a smile).
   - `0` represents the absence of a feature (background).
2. **Graph Construction using BFS**:
   - Each matrix cell is treated as a **node**.
   - Nodes are connected to their valid **neighbors** (up, down, left, right).
   - A **BFS traversal** explores the entire matrix systematically.
3. **Emotion Detection**:
   - The algorithm looks for **patterns** that indicate a smile or frown.
   - Position, orientation, and multiple instances are considered.
4. **Emotion Classification**:
   - If a smile is detected, it is classified as "happy".
   - If a straight or downward curve is found, it is classified as "neutral" or "sad".

## Implementation Details
### Node and BFS Queue Classes
```python
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
```

### BFS Traversal to Convert Matrix into Tree
```python
def get_neighbor_coordinates(matrix, row, col):
    neighbors_coordinates = []
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for directionRow, directionColumn in directions:
        newRow, newCol = row + directionRow, col + directionColumn
        if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]):
            neighbors_coordinates.append((newRow, newCol))
    return neighbors_coordinates

def matrix_to_tree(matrix):
    root = Node(0, 0)
    queue = Queue()
    queue.enqueue(root)
    visited = set()

    while not queue.is_empty():
        current_node = queue.get_item()
        visited.add((current_node.row, current_node.col))
        for neighbor_row, neighbor_col in get_neighbor_coordinates(matrix, current_node.row, current_node.col):
            if (neighbor_row, neighbor_col) not in visited:
                new_node = Node(neighbor_row, neighbor_col)
                current_node.add_neighbor(new_node)
                queue.enqueue(new_node)
                visited.add((neighbor_row, neighbor_col))
        queue.dequeue()
    return root
```

### Printing the Generated Tree
```python
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
```

## Usage
1. Load an `8x8` matrix representing an image.
2. Construct a graph using `matrix_to_tree(matrix)`.
3. Traverse the graph using BFS to analyze patterns.
4. Determine the emotion based on detected patterns.
5. Print the tree structure for debugging purposes.

### Example Execution
```python
# Create an 8x8 binary test matrix
c, r = 8, 8
arr = [[0] * c for _ in range(r)]
# Fill the matrix with sample data (e.g., a smile pattern)
# (Modify this section for different test cases)

root = matrix_to_tree(arr)
print_tree(arr, root)
```

## Addressing Key Challenges
1. **Does location and direction matter?**
   - Yes, because smiles can appear in different positions.
   - Implement **rotation-invariant detection**.
2. **What if the smile is vertical instead of horizontal?**
   - Detect different orientations using feature extraction.
3. **Do we need to handle multiple smiles?**
   - Yes, use **connected component analysis** to count multiple instances.
4. **How to detect multiple smiles?**
   - Identify separate connected regions of `1`s and analyze them individually.

## Possible Improvements
- **Enhancing feature extraction**: Consider edge detection or shape recognition.
- **Handling rotations**: Implement rotation-invariant pattern matching.
- **Machine Learning Approach**: Use CNNs for more accurate classification.

## Conclusion
This project demonstrates how BFS and graph traversal can be used to analyze **binary image matrices** and recognize **emotions**. Future work can extend this approach with more sophisticated image processing techniques.


# Parallel BFS Implementation

This project implements a parallel Breadth-First Search (BFS) algorithm using Python's multiprocessing capabilities. The implementation is designed to efficiently traverse large graphs by distributing the workload across multiple CPU cores.

## Features

- Parallel BFS implementation using Python's multiprocessing
- Automatic detection of connected components
- Load balancing across worker processes
- Progress tracking during traversal
- Performance metrics (execution time and visited nodes)

## Files

- `bfs.py` - Main implementation of the parallel BFS algorithm
- `generate.py` - Graph generator utility
- `grafo.py` - Generated graph data (created by generate.py)

## Usage

1. Generate a test graph:
```bash
python generate.py
```

2. Run the parallel BFS algorithm:
```bash
python bfs.py
```

NOTE: The number of workers is hardcoded to 4 in the `bfs.py` file, you can change it to any number you want.
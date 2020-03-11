import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def calculatePath(tile1, tile2, map):
    matrix = [[1 for x in range(map.height)] for y in range(map.width)]
    for x in range(map.width):
        for y in range(map.height):
            # print("hello")
            if len(map.tiles[x][y].objects) != 0:
                matrix[x][y] = 0
            else:
                matrix[x][y] = 1

    # 0 - obstacle
    # >0 - weight
    # start and end shouldn't be 0's

    grid = Grid(matrix=matrix)

    start = grid.node(tile1.x, tile1.y)
    end = grid.node(tile2.x, tile2.y)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    # print(grid.grid_str)

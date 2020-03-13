import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


def calculatePath(tile1, tile2, map):
    # matrix = [[1 for x in range(map.height)] for y in range(map.width)]
    matrix = [[1 for x in range(map.width)] for y in range(map.height)]
    for x in range(map.width):
        for y in range(map.height):
            if map.tiles[x][y].objects and (tile1.x != x or tile1.y != y) and (tile2.x != x or tile2.y != y):
                for obj in map.tiles[x][y].objects:
                    if obj.blocks:
                        matrix[y][x] = 0
            else:
                matrix[y][x] = 1

    grid = Grid(matrix=matrix)

    start = grid.node(tile1.x, tile1.y)
    end = grid.node(tile2.x, tile2.y)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)

    print('operations:', runs, 'path length:', len(path))
    print(grid.grid_str(path=path, start=start, end=end))
    # print(grid.grid_str)
    return path
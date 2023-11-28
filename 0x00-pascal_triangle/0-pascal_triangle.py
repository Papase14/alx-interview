#!/usr/bin/python3
"""
Pascal Triangle
"""

def pascal_triangle(n):
    """
    Generates a Pascal's triangle up to a given number of rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list representing the Pascal's triangle with `n` rows.

    Example:
        >>> pascal_triangle(5)
        [[1],
         [1, 1],
         [1, 2, 1],
         [1, 3, 3, 1],
         [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

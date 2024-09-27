"""
Program to solve kattis problem:
Finds traingle's area given height and base.

Author: Ram Basnet
Date:
CSCI 110 - CS0 

# Algorithm steps:
# 1. use a function to read the height and base as a line
# 2. use a function to split line into two integers
#   a. convert each substring into int
#   b. return those ints
# 3. use funtion to find area = (height*base)/2 and reuturn the result
# 4. print area
"""

import sys


def readline() -> str:
    """Reads a line and returns it.

    Returns:
        str: line
    """
    # 1. define readline
    line = input()
    return line


def area_triangle(height: int, base: int) -> float:
    """_summary_

    Args:
        height (int): _description_
        base (int): _description_

    Returns:
        float: _description_
    """
    # 3
    area = (height*base)/2
    return area


def splitline(line):
    # 2
    # 2.a
    h, b = line.split()
    print(f'{h=}', f'{b=}', file=sys.stderr)
    # 2.b
    height = int(h)
    base = int(b)
    return height, base


def main() -> None:
    # 1. use readline
    data = readline()
    print(f'{data=}', file=sys.stderr)
    # 2. use splitline
    height, base = splitline(data)
    area = area_triangle(height, base)
    print(area)


if __name__ == '__main__':
    main()

"""Test module for triarea
"""

import triarea


def test_tri_area() -> None:
    """_summary_
    """
    ans = triarea.area_triangle(2, 3)
    assert ans == 3.0, f'{ans} != 3.0'


def test_tri_area_1():
    """_summary_
    """
    assert triarea.area_triangle(3, 3) == 4.5, 'not equal'

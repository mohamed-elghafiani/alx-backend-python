#!/usr/bin/env python3
"""Module for safely_get_value function"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom array"""
    zoomed_in: List = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3.0)

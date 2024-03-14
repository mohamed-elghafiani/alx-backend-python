#!/usr/bin/env python3
"""Module for annotated variables"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates sum of lists of floats and ints"""
    return sum(mxd_lst)

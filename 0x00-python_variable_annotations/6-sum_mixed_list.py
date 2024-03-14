#!/usr/bin/env python3
"""Module for annotated variables"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """Calculates sum of lists of floats"""
    return sum(mxd_list)

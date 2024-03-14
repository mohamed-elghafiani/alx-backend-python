#!/usr/bin/env python3
"""Module for element_length function"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns elements length"""
    return [(i, len(i)) for i in lst]

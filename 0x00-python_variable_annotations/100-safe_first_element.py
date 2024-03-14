#!/usr/bin/env python3
"""Module for safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function where the types of the elements of the input are not known"""
    if lst:
        return lst[0]
    else:
        return None

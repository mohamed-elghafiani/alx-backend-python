#!/usr/bin/env python3
"""Module for safely_get_value function"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')
def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Typed dict mapping function
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""
  0x02. Python - Async Comprehension
  Task #1: Async Comprehensions
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns numbers using an async comprehensing over async_generator"""
    res = [i async for i in async_generator()]
    return res

#!/usr/bin/env python3
"""
  0x02. Python - Async Comprehension
  Task #2: Run time for four parallel comprehensions
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Calculates the runtime for four parallel comprehensions"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter() - start
    return end

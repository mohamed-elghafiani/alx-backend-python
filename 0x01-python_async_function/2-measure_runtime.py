#!/usr/bin/env python3
"""
  0x01. Python - Async
  Task #2: Measure the runtime
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the time elapsed by wait_n()

      Args:
       n: int
       max_delay: int

      Returns:
       The time elapsed
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start

    return end/n

#!/usr/bin/env python3
"""0x01 Python - Async
   Task #1: Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple coroutines at the same time with async
       Args:
        n: int
        max_delay: int

       Returns:
        The list of all the delays (float values)
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

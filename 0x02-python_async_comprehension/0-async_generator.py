#!/usr/bin/env python3
"""
  0x02. Python - Async Comprehension
  Task #0: Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async range()"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3
"""0x01. Python - Async
   Task #0
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """asynchronous coroutine that waits for a random delay [0, max_delay]"""
    delay = random.rand(0, max_delay)

    await asyncio.sleep(delay)
    return delay

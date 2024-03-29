#!/usr/bin/env python3
"""
  0x01. Python - Async
  Task #3: Tasks
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task

      Args:
       max_delay: int

      Returns:
       a asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

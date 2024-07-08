#!/usr/bin/env python3
"""he function task_wait_n asynchronously waits for
multiple tasks to complete and returns their delays."""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create a list of futures, each of which is a Task that
    waits for a random delay up to max_delay seconds."""
    fut = [task_wait_random(max_delay) for _ in range(n)]
    fut = asyncio.as_completed(fut)
    hold_ti = [await future for future in fut]
    return hold_ti

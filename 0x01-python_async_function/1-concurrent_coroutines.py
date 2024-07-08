#!/usr/bin/env python3
"""The function wait_n asynchronously waits for random
delays and returns them in order of completion."""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """reate a list of futures, each of which is a coroutine that
    waits for a random delay up to max_delay seconds."""
    fut = [wait_random(max_delay) for _ in range(n)]
    fut = asyncio.as_completed(fut)
    del_get = [await future for future in fut]
    return del_get

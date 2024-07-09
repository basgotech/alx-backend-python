#!/usr/bin/env python3
"""The function measure_runtime measures the total runtime
of executing async_comprehension four times concurrently.
"""
import asyncio
import time
async_comprehensions = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times
    concurrently using asyncio.gather."""
    ready_t = time.perf_counter()
    await asyncio.gather(async_comprehensions(), async_comprehensions(),
                         async_comprehensions(), async_comprehensions())
    return time.perf_counter() - ready_t

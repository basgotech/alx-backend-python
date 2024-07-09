#!/usr/bin/env python3
"""The function async_comprehension uses an async
comprehension to collect and return values from
an async generator."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use an async comprehension to collect all
    values generated by async_generator into a list."""
    return [_ async for _ in async_generator()]
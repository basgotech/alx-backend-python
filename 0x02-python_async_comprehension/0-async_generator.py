#!/usr/bin/env python3
"""The function async_generator is an asynchronous
generator that yields random floats."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times to yield 10 random numbers."""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

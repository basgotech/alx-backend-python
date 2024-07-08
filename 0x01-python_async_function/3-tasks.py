#!/usr/bin/env python3
"""The function task_wait_random creates an asyncio
Task for a coroutine that waits for a random delay."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a Task that will run the wait_random
    coroutine with the given max_delay."""
    return asyncio.create_task(wait_random(max_delay))

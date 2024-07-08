#!/usr/bin/env python3
"""The function measure_time calculates the average time
taken to complete a set of asynchronous tasks."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run the wait_n function, which waits for n random
    delays up to max_delay seconds."""
    run_up = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    landing = time.perf_counter()
    return (landing - run_up) / n

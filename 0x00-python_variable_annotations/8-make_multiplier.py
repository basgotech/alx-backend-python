#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument
    """
    def f(b: float) -> float:
        """ multiplies a float by multiplier """
        return float(b * multiplier)

    return f

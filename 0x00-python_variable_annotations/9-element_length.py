#!/usr/bin/env python3
""" iterable object"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Element of length """
    return [(x, len(x)) for x in lst]

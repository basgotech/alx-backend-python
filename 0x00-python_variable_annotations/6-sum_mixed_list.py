#!/usr/bin/env python3

""" Mixed list - sum of integers and floats """

from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Takes a mixed list `mxd_lst` of integers and floats
    and returns their sum as a float. """
    return float(sum(mxd_lst))

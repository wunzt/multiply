# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/24/2022
# Description: Function returns the product of two positive integers.

def multiply(num_1, num_2):
    """Returns the product of two positive integers."""

    if num_2 == 1:
        return num_1

    return num_1 + multiply(num_1, num_2-1)
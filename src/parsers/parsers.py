from re import search
from patterns import *

def coefficients_parser(input):
    # type: (str) -> input
    lines = input.split('\n')

    result = []

    for line in lines:
        matches = search(coefficients_pattern, line).groups()
        result.append(matches)

    return result

from re import search
from patterns import *

def coefficients_parser(input):
    # type: (str) -> input
    lines = input.split('\n')

    result = []

    for line in lines:
        matches = search(coefficients_pattern, line).groups()
        numbers = map(lambda x: float(x) if '.' in x else int(x), matches)
        result.append(numbers)

    return result

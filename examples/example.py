#!/usr/bin/python
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from postg_parser.parsers import coefficients_parser

coefficients_part_for_acetilen = (
    '  1   1  0.000000E+00  2.678809217E+01  9.052548035E+02  2.947495885E+04  5.759574E+00  6.425197E+00\n'
    '  1   2  2.022007E+00  7.199756335E+00  2.016031754E+02  5.971516229E+03  5.366860E+00  6.129091E+00\n'
    '  1   3  2.269939E+00  2.678809217E+01  9.052548035E+02  2.947495885E+04  5.759574E+00  6.425197E+00\n'
    '  1   4  4.291946E+00  7.199756335E+00  2.016031754E+02  5.971516229E+03  5.366860E+00  6.129091E+00\n'
    '  2   2  0.000000E+00  1.935095969E+00  4.297770348E+01  1.201940150E+03  4.997762E+00  5.850791E+00\n'
    '  2   3  4.291946E+00  7.199756335E+00  2.016031754E+02  5.971516229E+03  5.366860E+00  6.129091E+00\n'
    '  2   4  6.313953E+00  1.935095969E+00  4.297770348E+01  1.201940150E+03  4.997762E+00  5.850791E+00\n'
    '  3   3  0.000000E+00  2.678809217E+01  9.052548035E+02  2.947495885E+04  5.759574E+00  6.425197E+00\n'
    '  3   4  2.022007E+00  7.199756335E+00  2.016031754E+02  5.971516229E+03  5.366860E+00  6.129091E+00\n'
    '  4   4  0.000000E+00  1.935095969E+00  4.297770348E+01  1.201940150E+03  4.997762E+00  5.850791E+00'
)

result = coefficients_parser(coefficients_part_for_acetilen)

print result

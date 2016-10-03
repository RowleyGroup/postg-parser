#!/usr/bin/python
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from postg_parser.postg import PostG

string = open('acetilen.postg').read()

postg = PostG(string)

print 'The molecule has %d atoms.' % len(postg.molecule.atoms)

print 'C6 Coefficients matrix:'
print postg.coefficients.c6

print 'C6 diagonal elements:'
print postg.coefficients.c6.diagonal()

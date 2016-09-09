#!/usr/bin/python
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from postg_parser.parsers import atoms_positions_parser

atoms_positions_part_for_acetilen = (
    "   1 C        0.0000000       0.0000000       1.1349695     60    194\n"
    "   2 H        0.0000000       0.0000000       3.1569765     40    194\n"
    "   3 C        0.0000000       0.0000000      -1.1349695     60    194\n"
    "   4 H        0.0000000       0.0000000      -3.1569765     40    194"
)

mol = atoms_positions_parser(atoms_positions_part_for_acetilen)

print 'Number of atoms: %d' % mol.OBMol.NumAtoms()

for atom in mol:
    print atom.OBAtom.GetAtomicNum()

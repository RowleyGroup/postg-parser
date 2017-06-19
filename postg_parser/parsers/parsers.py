from re import search
from .patterns import *
from openbabel import OBMol, OBElementTable
from pybel import Molecule
from numpy import matrix, zeros
from math import sqrt
from ..coefficients import Coefficients


def item_set(matrix, position, value):
    i, j = position
    matrix.itemset((i, j), value)

    if i != j:
        matrix.itemset((j, i), value)


def coefficients_parser(input):
    """
    :param input: The input string
    :type input: str
    :rtype: matrix
    """
    lines = input.split('\n')
    number_of_atoms = int(int(sqrt(1 + 8 * len(lines)) - 1) / 2)

    c6 = matrix(zeros(shape=(number_of_atoms, number_of_atoms)))
    c8 = matrix(zeros(shape=(number_of_atoms, number_of_atoms)))
    c10 = matrix(zeros(shape=(number_of_atoms, number_of_atoms)))
    rvdw = matrix(zeros(shape=(number_of_atoms, number_of_atoms)))

    for line in lines:
        matches = search(coefficients_pattern, line).groups()
        numbers = list(map(lambda x: float(x) if '.' in x else int(x), matches))
        i = numbers[0] - 1
        j = numbers[1] - 1

        item_set(c6, [i, j], numbers[3])
        item_set(c8, [i, j], numbers[4])
        item_set(c10, [i, j], numbers[5])
        item_set(rvdw, [i, j], numbers[7])

    return Coefficients(c6=c6, c8=c8, c10=c10, rvdw=rvdw)


def atoms_positions_parser(input):
    """
    :param input: The input string
    :type input: str
    :rtype: Molecule
    """
    lines = input.split('\n')

    element_table = OBElementTable()
    mol = OBMol()

    for line in lines:
        matches = search(atoms_positions_pattern, line)

        # Create the atom
        atom = mol.NewAtom()

        # Set the proper atomic number with respect of the atomic symbol
        atomic_number = element_table.GetAtomicNum(matches.group(2))
        atom.SetAtomicNum(atomic_number)

        # Set the atom vector
        x = float(matches.group(3))
        y = float(matches.group(4))
        z = float(matches.group(5))
        atom.SetVector(x, y, z)

    return Molecule(mol)

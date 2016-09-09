from re import search
from patterns import *
from openbabel import OBMol, OBElementTable
from pybel import Molecule


def coefficients_parser(input):
    """
    :param input: The input string
    :type input: str
    :rtype: list
    """
    lines = input.split('\n')

    result = []

    for line in lines:
        matches = search(coefficients_pattern, line).groups()
        numbers = map(lambda x: float(x) if '.' in x else int(x), matches)
        result.append(numbers)

    return result


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

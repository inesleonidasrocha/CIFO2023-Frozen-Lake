from random import random, randint, sample

def scramble_mutation(individual):
    """
    Scrambled mutation for a GA individual. Scrambles a portion of the representation.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Here we chose a random window 
    mut_indexes = sample(range(0, len(individual)), 2)
    mut_indexes.sort()
    # Scramble the selected section       
    individual[mut_indexes[0]:mut_indexes[1]] = random.sample(individual[mut_indexes[0]:mut_indexes[1]], mut_indexes[1] - mut_indexes[0]) 
    return  individual


def swap_mutation(individual):
    """
    Swap mutation for a GA individual. Swaps the bits.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    mut_indexes = sample(range(0, len(individual)), 2)
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]
    return individual


def inversion_mutation(individual):
    """
    Inversion mutation for a GA individual. Reverts a portion of the representation.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    mut_indexes = sample(range(0, len(individual)), 2)
    mut_indexes.sort()
    individual[mut_indexes[0]:mut_indexes[1]] = individual[mut_indexes[0]:mut_indexes[1]][::-1]
    return individual

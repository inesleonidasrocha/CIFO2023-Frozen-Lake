import random
from random import sample

def scramble_mutation(individual):
    """
    Performs scrambled mutation on a GA individual by scrambling a portion of its representation.
      
    Args:
        individual (Individual): A GA individual from charles.py
        
    Returns:
        Individual: Mutated Individual       
    """  
    # Select a random window
    mut_indexes = sample(range(0, len(individual)), 2)
    mut_indexes.sort()
    # Scramble the selected section       
    individual[mut_indexes[0]:mut_indexes[1]] = random.sample(individual[mut_indexes[0]:mut_indexes[1]], mut_indexes[1] - mut_indexes[0]) 
    return  individual


def swap_mutation(individual):
    """
    Performs swap mutation on a GA individual representation by swapping values 
    at two randomly selected positions. 

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Select two random positions
    mut_indexes = sample(range(0, len(individual)), 2)
    # Swap the values at the selected positions
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]
    return individual


def inversion_mutation(individual):
    """
    Perform inversion mutation on a GA individual representation by   
    reversing a portion of it.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Select a random window
    mut_indexes = sample(range(0, len(individual)), 2)
    mut_indexes.sort()
     # Reverse the portion between the selected positions
    individual[mut_indexes[0]:mut_indexes[1]] = individual[mut_indexes[0]:mut_indexes[1]][::-1]
    return individual

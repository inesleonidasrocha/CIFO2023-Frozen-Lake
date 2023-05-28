import random
from random import randint, sample, uniform
import numpy as np

"""
Crossover Methods

References: 
https://medium.com/@samiran.bera/crossover-operator-the-heart-of-genetic-algorithm-6c0fdcb405c0
https://www.geeksforgeeks.org/crossover-in-genetic-algorithm/
https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_crossover.htm
http://www.tomaszgwiazda.com/heuristicX.htm
https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8
"""

def arithmetic_xo(p1, p2):
    """
    Implementation of arithmetic crossover/geometric crossover with constant alpha.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Generating alpha as random value between 0 and 1
    alpha = uniform(0, 1)

    # Initializings offsprings as empty lists
    o1 = [None] * len(p1)
    o2 = [None] * len(p1)

    for i in range(len(p1)):
        # Offsprings are the weighted averages of the parents  
        o1[i] = int(round(p1[i] * alpha + (1-alpha) * p2[i],0))
        o2[i] = int(round(p2[i] * alpha + (1-alpha) * p1[i],0))
    return o1, o2


def single_point_xo(p1, p2, co_point=None):
    """
    Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

     Keyword Args:
        co_point (int, optional):  
           - co_point = None  if called directly 
           - Otherwise, co_point from multi_point_xo() call

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    if co_point is None:
        # Selects a random crossover point   
        co_point = randint(1, len(p1)-2)

    # Offspring 1 is combination of p1 up to co_point and p2 after
    o1 = p1[:co_point] + p2[co_point:]
    # Offspring 2 is combination of p2 up to co_point and p1 after
    o2 = p2[:co_point] + p1[co_point:]

    return o1, o2


def multi_point_xo(p1, p2): 
    """
    Performs multi-point crossover.
      
    Args: 
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
        
    Returns:
        Individuals: Two offspring, resulting from crossover.  
    """
    num_points = 5  # Number of crossover points

    # Select num_points crossover points at random indices
    xo_indexes = sorted(sample(range(0, len(p1)), num_points))
    
    # Initializings offspring as copies of the parents 1 and 2 respectively
    o2 = p2.copy()
    
    for i in xo_indexes:
        # Performing single point crossover at each index 
        o1, o2 = single_point_xo(o1, o2, i)  
        
    return o1, o2


def uniform_xo(p1, p2): 
    """
    Performs uniform crossover.
    
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
        
    Returns:
        Individuals: Two offspring, resulting from crossover.        
    """
    for i in range(len(p1)):
        # With 50% probability, swap genes between parents
        if np.random.rand(1) < 0.5:
           
            # Store current p1 gene in a temporary variable
             aux = p1[i]
            # Assigning p2 gene to p1 
             p1[i] = p2[i]
            # Assigning temp (original p1) to p2
             p2[i] = aux
    
    return p1,p2


def crossover_mask(chrom_len):
    """
    Generates a crossover mask of boolean values.
    
    Args:
        chrom_len (int): Length of chromosome. 
        
    Returns: 
        numpy array: Crossover mask of boolean values.
    """ 
    return np.random.rand(chrom_len) >= 0.5

def uniform_mask_xo(p1,p2):
    """
    Perform uniform crossover with a mask. 
    
    Args:
        p1 (Individual): First parent for crossover.  
        p2 (Individual): Second parent for crossover.
        
    Returns:
        Individuals: Two offspring from crossover.
    """  
    # Generates a mask based on the individual length    
    mask = crossover_mask(len(p1))

    for i in range(len(p1)):
        # If mask value is True, swap genes between parents
        if mask[i]:
            aux = p1[i] 
            p1[i] = p2[i] 
            p2[i] = aux
    return p1,p2


def heuristic_xo(p1, p2):
    '''
    Performs heuristic crossover on parents.
    The offspring inherit genes based on heuristic rules.
   
    Args:
        p1 (Individual): First parent for crossover.     
        p2 (Individual): Second parent for crossover.
            
    Returns:
        Individuals: Two offspring, from crossover.
    '''
    
    def get_heuristic_offspring_v1(p1, p2):
        #Initializes offspring as an empty list
        offspring = []
        # Generate offspring based on heuristic rules below
        for i in range(len(p1)):
            if p1[i] == p2[i]:
                offspring.append(p1[i])  # Inherit the same value from both parents
            else:
                # Apply a heuristic rule based on the problem domain
                # In this instance, we use the average of the two values
                value = int(round((p1[i] + p2[i]) / 2,0))
                if value > 3:
                    value = 3  # Limit the value to the maximum allowed
                offspring.append(value)
        return offspring
    
    # Calling function twice to generate 2 offsprings 
    o1, o2 = get_heuristic_offspring_v1(p1, p2), get_heuristic_offspring_v1(p1, p2)
    return o1, o2

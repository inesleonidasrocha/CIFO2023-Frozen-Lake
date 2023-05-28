import random
from random import randint, sample, uniform
import numpy as np

def arithmetic_xo(p1, p2):
    """
    Implementation of arithmetic crossover/geometric crossover with constant alpha.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    alpha = uniform(0, 1)
    o1 = [None] * len(p1)
    o2 = [None] * len(p1)
    for i in range(len(p1)):
        o1[i] = int(round(p1[i] * alpha + (1-alpha) * p2[i],0))
        o2[i] = int(round(p2[i] * alpha + (1-alpha) * p1[i],0))
    return o1, o2


def single_point_xo(p1, p2, co_point=None):
    """
    Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    if co_point is None:
        co_point = randint(1, len(p1)-2)

    o1 = p1[:co_point] + p2[co_point:]
    o2 = p2[:co_point] + p1[co_point:]

    return o1, o2


def multi_point_xo(p1, p2): #num_points):
    num_points = 5  # Number of crossover points
    
    xo_indexes = sorted(sample(range(0, len(p1)), num_points))
    
    o1 = p1.copy()
    o2 = p2.copy()
    
    for i in xo_indexes:
        o1, o2 = single_point_xo(o1, o2, i)  
        
    return o1, o2


def uniform_xo(p1, p2): 
    for i in range(len(p1)):
        if np.random.rand(1) < 0.5:
             aux = p1[i]
             p1[i] = p2[i]
             p2[i] = aux
    
    return p1,p2


def crossover_mask(chrom_len):
    return np.random.rand(chrom_len) >= 0.5

def uniform_mask_xo(p1,p2):    
    mask = crossover_mask(len(p1))

    for i in range(len(p1)):
        if mask[i]:
            aux = p1[i] 
            p1[i] = p2[i] 
            p2[i] = aux
    return p1,p2


def heuristic_xo(p1, p2):
    
    def get_heuristic_offspring_v1(p1, p2):
        offspring = []
        for i in range(len(p1)):
            if p1[i] == p2[i]:
                offspring.append(p1[i])  # Inherit the same value from both parents
            else:
                # Apply a heuristic rule based on the problem domain
                # For this example, let's use the average of the two values
                value = int(round((p1[i] + p2[i]) / 2,0))
                if value > 3:
                    value = 3  # Limit the value to the maximum allowed
                offspring.append(value)
        return offspring

    o1, o2 = get_heuristic_offspring_v1(p1, p2), get_heuristic_offspring_v1(p1, p2)
    return o1, o2

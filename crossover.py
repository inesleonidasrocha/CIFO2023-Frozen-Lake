from random import randint, sample, uniform
import numpy as np

def arithmetic_xo(p1, p2):
    """Implementation of arithmetic crossover/geometric crossover with constant alpha.

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

def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2


def uniform_xo(p1, p2): 
    for i in range(len(p1)):
        if np.random.rand(1) < 0.5:
             aux = p1[i]
             p1[i] = p2[i]
             p2[i] = aux
    
    return p1,p2
    
    
'''if __name__ == '__main__':
    p1, p2 = [0, 0, 0, 0], [2, 2, 2,2]
    o1, o2 = uniform_xo(p1, p2)
    print(o1, o2)'''




















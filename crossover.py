from random import randint, sample, uniform
import numpy as np
from FL_fitness import get_fitness
from charles import Individual


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

def single_point_co(p1, p2, co_point=None):
    """Implementation of single point crossover.

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

def multi_point_crossover(p1, p2): #num_points):
    num_points = 5  # Number of crossover points
    
    xo_indexes = sorted(sample(range(0, len(p1)), num_points))
    
    o1 = p1.copy()
    o2 = p2.copy()
    
    for i in xo_indexes:
        o1, o2 = single_point_co(o1, o2, i)  
        
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

def mask_xo(p1,p2):    
    mask = crossover_mask(len(p1))

    for i in range(len(p1)):
        if mask[i]:
            aux = p1[i] 
            p1[i] = p2[i] 
            p2[i] = aux
    return p1,p2

def heuristic_xo(p1, p2):
    # Calculate weight based on fitness difference
    fitness_diff = abs(p1.fitness - p2.fitness)
    w = 1 - fitness_diff / min(p1.fitness, p2.fitness)
    
    offspring = []
    
    # Loop through each gene
    for i in range(len(p1)):
        # Favor the better parent for that gene
        if p1[i] == p2[i]: 
            offspring.append(p1[i]) 
        elif p1.fitness < p2.fitness:
            offspring.append(p1[i])
        else:
            offspring.append(p2[i])
            
    # Apply weighted average for genes that differ        
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            offspring[i] = int(abs(round(w * p1[i] + (1-w) * p2[i],0)))
            
    return Individual(offspring) 


      
    
'''if __name__ == '__main__':
    #p1, p2 = [0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0,0,0,0,0], [2, 2, 2,2,2, 2, 2,2,2, 2, 2,2,3,3,3,3]
    #o1, o2 = multi_point_crossover(p1, p2)
    #o3,o4 = single_point_co(p1, p2)
    p1 = Individual()
    p2 = Individual()
    o1,o2 = heuristic_xo(p1,p2)
    print(o1, o2)
    #print(o3, o4)'''




















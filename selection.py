import random
from random import uniform, choice
from operator import attrgetter
"""
Selection Methods

References: 
https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm
"""

def tournament_sel(population, size=4):
    """
    Performs tournament selection to select an individual from the population.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: The best individual in the tournament.
    """

    # Select individuals based on tournament size with choice, there is a possibility of repetition in the choices,
    # so every individual has a chance of getting selected
    tournament = [choice(population.individuals) for _ in range(size)]

    # Select the best individual from the tournament
    if population.optim == "max":
        return max(tournament, key = attrgetter("fitness"))
    if population.optim == "min":
        return min(tournament, key = attrgetter("fitness"))


def roulette_selection(population):
    """
    Perform roulette wheel selection to select an individual from the population.
       
    Args:     
        population (Population): The population to select from  
    Returns:     
        Individual: The selected individual    
    """
    # Determine the range of fitness values
    min_fitness = min(population.individuals, key=attrgetter("fitness")).fitness
    
    # Adjust fitness values to prevent worst individuals from being excluded. 
    # Normalize fitness values to preserve diversity
    adjusted_fitness = [chromo.fitness - min_fitness +1 for chromo in population.individuals]

    # Calculate the total fitness
    total_fitness = sum(adjusted_fitness)       

    # Generate a random number between 0 and total fitness 
    random_num = random.uniform(0, total_fitness)
      
    cumulative_sum = 0           
    for i, fitness in enumerate(adjusted_fitness):      
        cumulative_sum += fitness              
        if cumulative_sum >= random_num:        
            if population.optim == "min":
                return min(population.individuals, key=attrgetter("fitness"))  
            else:
                return population.individuals[i] 

        
def rank_selection(population):
    """
    Performs rank selection to select an individual from the population.
   
    Args:     
        population (Population): The population to select from           
    Returns:     
        Individual: The selected individual       
    """
    # Sorts the population in ascending order by fitness      
    sorted_population = sorted(population.individuals, key=attrgetter("fitness"), reverse=True)
    
    # Calculate cumulative probabilities for each individual based on their ranks.
    total_ranks = sum([i for i in range(1, len(sorted_population) + 1)])
    cumulative_probabilities = [(len(sorted_population) - i) / total_ranks for i in range(0, len(sorted_population))]
    
    # Generates a random number
    random_num = random.uniform(0, 1)
    
    # Performs rank selection
    cumulative_sum = 0
    for i, chromo in enumerate(sorted_population):
        cumulative_sum += cumulative_probabilities[i]
        if cumulative_sum >= random_num: 
                if population.optim == "max":                   
                    return chromo
                return min(sorted_population, key=attrgetter("fitness"))

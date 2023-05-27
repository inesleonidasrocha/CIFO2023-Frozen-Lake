import random
from random import uniform, choice
from operator import attrgetter

def tournament_sel(population, size=4):
    """
    Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: The best individual in the tournament.
    """

    # Select individuals based on tournament size with choice, there is a possibility of repetition in the choices,
    # so every individual has a chance of getting selected
    tournament = [choice(population.individuals) for _ in range(size)]

    # With sample, there is no repetition of choices
    # tournament = sample(population.individuals, size)
    if population.optim == "max":
        return max(tournament, key = attrgetter("fitness"))
    if population.optim == "min":
        return min(tournament, key = attrgetter("fitness"))


def roulette_selection(population):
    # Determine the range of fitness values
    min_fitness = min(population.individuals, key=attrgetter("fitness")).fitness
    
    # Adjust the fitness values substracting minimum fitness
    # Worst value can be picked because we dont want to lose diversity. The number is lower than the rest (1)
    adjusted_fitness = [chromo.fitness - min_fitness +1 for chromo in population.individuals]

    # Calculate the total fitness
    total_fitness = sum(adjusted_fitness)       

    # Generate a random number
    random_num = random.uniform(0, total_fitness)

    # Perform roulette wheel selection
    cumulative_sum = 0
    for i, fitness in enumerate(adjusted_fitness):
        cumulative_sum += fitness
        if cumulative_sum >= random_num:
            return population.individuals[i]  # Return the selected individual

        
def rank_selection(population):
    # Sort the population by fitness
    sorted_population = sorted(population.individuals, key=attrgetter("fitness"), reverse=True)
    
    # Calculate cumulative probabilities for each individual based on their ranks.
    total_ranks = sum([i for i in range(1, len(sorted_population) + 1)])
    cumulative_probabilities = [(len(sorted_population) - i) / total_ranks for i in range(0, len(sorted_population))]
    
    # Generate a random number
    random_num = random.uniform(0, 1)
    
    # Perform rank selection
    cumulative_sum = 0
    for i, chromo in enumerate(sorted_population):
        cumulative_sum += cumulative_probabilities[i]
        if cumulative_sum >= random_num:
            return chromo

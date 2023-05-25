import random
from random import uniform, choice
from operator import attrgetter


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":

        # Sum total fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        raise NotImplementedError

    else:
        raise Exception("No optimization specified (min or max).")


def tournament_sel(population, size=4):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: The best individual in the tournament.
    """

    # Select individuals based on tournament size
    # with choice, there is a possibility of repetition in the choices,
    # so every individual has a chance of getting selected
    tournament = [choice(population.individuals) for _ in range(size)]

    # with sample, there is no repetition of choices
    # tournament = sample(population.individuals, size)
    if population.optim == "max":
        return max(tournament, key=attrgetter("fitness"))
    if population.optim == "min":
        return min(tournament, key=attrgetter("fitness"))


def roulette_selection(population):
    # Step 1: Determine the range of fitness values
    min_fitness = min(population.individuals, key=attrgetter("fitness")).fitness
    
    # Step 2: Adjust the fitness values substracting minimum fitness
    # Worst value can be picked because we dont want to lose diversity. The number is lower than the rest (1)
    adjusted_fitness = [chromo.fitness - min_fitness +1 for chromo in population.individuals]

    # Step 3: Calculate the total fitness
    total_fitness = sum(adjusted_fitness)       

    # Step 4: Generate a random number
    random_num = random.uniform(0, total_fitness)

    # Step 5: Perform roulette wheel selection
    cumulative_sum = 0
    for i, fitness in enumerate(adjusted_fitness):
        cumulative_sum += fitness
        if cumulative_sum >= random_num:
            return population.individuals[i]  # Return the selected individual

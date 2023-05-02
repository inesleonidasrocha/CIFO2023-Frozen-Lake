from operator import attrgetter
from random import uniform, sample, choice


def fps(population):
    if population.optim == "max":
        total_fitness = sum([individual.fitness for individual in population])
        mark = uniform(0, total_fitness)
        position = 0
        for individual in population:
            position += individual.fitness
            if position > mark:
                return individual


def tournament_sel(population, size=4):
    # tournament = sample(population.individuals, size)
    tournament = [choice(population.individuals) for _ in range(size)]
    if population.optim == "max":
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == "min":
        return min(tournament, key=attrgetter("fitness"))

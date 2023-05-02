from copy import deepcopy

from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from data.tsp_data import distance_matrix, cities


def get_fitness(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """
    fitness = 0
    for i in range(len(self.representation)):
        fitness += distance_matrix[self.representation[i - 1]][self.representation[i]]
    return int(fitness)


def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switches
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation) - 1)]

    for index, neighbour in enumerate(n):
        neighbour[index], neighbour[index + 1] = neighbour[index + 1], neighbour[index]

    n = [Individual(i) for i in n]
    return n


# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(
    size=1,
    sol_size=len(cities),
    valid_set=[i for i in range(len(cities))],
    # for traveling sales person we don't want repetitions o replacement = false
    replacement=False,
    optim="min")

#hill_climb(pop)
sim_annealing(pop)

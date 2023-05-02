from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from copy import deepcopy
from data.ks_data import weights, values, capacity


def get_fitness(self):
    """A function to calculate the total weight of the bag if the capacity is not exceeded
    If the capacity is exceeded, it will return a negative fitness
    Returns:
        int: Total weight
    """
    fitness = 0
    weight = 0
    for bit in range(len(self.representation)):
        if self.representation[bit] == 1:
            fitness += values[bit]
            weight += weights[bit]
    if weight > capacity:
        fitness = capacity - weight
    return fitness


def get_neighbours(self):
    """A neighbourhood function for the knapsack problem,
    for each neighbour, flips the bits
    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation))]

    for index, neighbour in enumerate(n):
        if neighbour[index] == 1:
            neighbour[index] = 0
        elif neighbour[index] == 0:
            neighbour[index] = 1

    n = [Individual(i) for i in n]
    return n


# Monkey Patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(size=1, optim="max", sol_size=len(values), valid_set=[0, 1], replacement=True)

hill_climb(pop)
sim_annealing(pop)
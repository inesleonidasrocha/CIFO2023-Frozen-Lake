from copy import deepcopy
from operator import attrgetter
from random import shuffle, choice, sample, random


class Individual:
    def __init__(
        self,
        representation=None,
        size=None,
        replacement=True,
        valid_set=None,
    ):
        if representation == None:
            if replacement == True:
                self.representation = [choice(valid_set) for i in range(size)]
            elif replacement == False:
                self.representation = sample(valid_set, size)
        else:
            self.representation = representation
        self.fitness = self.get_fitness()

    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def get_neighbours(self, func, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"


class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    replacement=kwargs["replacement"],
                    valid_set=kwargs["valid_set"],
                )
            )

    def evolve(self,gens,select,mutate,crossover,xc_prob,mut_prob,elitism):

        for i in range(gens):
            new_pop = []
            if elitism:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals,key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                    parent1, parent2 = select(self), select(self)

                    if random() < xc_prob:
                        offspring1, offspring2 = crossover(parent1, parent2)
                    else:
                        offspring1, offspring2 = parent1, parent2

                    # 0.2 mutation prob
                    if random() < mut_prob:
                        offspring1 = mutate(offspring1)
                    if random() < mut_prob:
                        offspring2 = mutate(offspring2)

                    new_pop.append(Individual(representation=offspring1))
                    if len(new_pop) < self.size:
                        new_pop.append(Individual(representation=offspring2))

            if elitism:
                if self.optim == "max":
                    worst = min(new_pop,key=attrgetter("fitness"))
                elif self.optim == "min":
                    worst = max(new_pop,key=attrgetter("fitness"))

                new_pop.pop(new_pop.index(worst))
                new_pop.append(elite)

            self.individuals = new_pop
            print(f'Best Individual:{max(self, key=attrgetter("fitness"))}')

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]
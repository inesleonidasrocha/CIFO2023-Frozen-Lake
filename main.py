from charles import Population, Individual
from selection import roulette_selection
from mutation import inversion_mutation
from crossover import pmx, cycle_xo, arithmetic_xo
from FL_fitness import get_fitness

Individual.get_fitness = get_fitness

pop = Population(
    size=50,
    optim="max",
    sol_size=16,
    valid_set=[0, 1, 2, 3],
    replacement=True,
)

for i in range(30):
    generations_fitness = []
    pop.evolve(gens=100, 
            xo_prob=0.9, 
            mut_prob=0.2, 
            select=roulette_selection,
            mutate=inversion_mutation, 
            crossover=arithmetic_xo,
            elitism=False)
    print("i just finishe run number: ", i+1)
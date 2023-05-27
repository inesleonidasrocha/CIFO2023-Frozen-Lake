import time
import matplotlib.pyplot as plt
from charles import Population, Individual
from FL_fitness import get_fitness
from selection import roulette_selection, tournament_sel, rank_selection
from crossover import arithmetic_xo, single_point_xo, multi_point_xo, uniform_xo, uniform_mask_xo, heuristic_xo
from mutation import scramble_mutation, swap_mutation, inversion_mutation

# Individual Monkey Patching
Individual.get_fitness = get_fitness

fitness_experiments = []

def run_experiment(population_size, generations, crossover_probability, mutation_probability, selection, mutation, 
                   crossover, elitism, replacement, slippery, sol_size = 16, valid_set = [0, 1, 2, 3]):

    iterations_fitness = []
    for i in range(50):
        start_time = time.time()
        
        # Create a population
        pop = Population(size = population_size, optim = "max", sol_size = sol_size, valid_set = valid_set,
                         replacement = replacement, slippery = slippery)

        # Evolve the population for 30 iterations
        iterations_fitness.append(pop.evolve(gens = generations, xo_prob=crossover_probability, mut_prob = mutation_probability,
                                             select=selection, mutate = mutation, crossover = crossover, elitism = elitism))
        
        end_time = time.time()  # Stop measuring the time
        iteration_time = end_time - start_time
        print(f"Iteration {i + 1} time: {round(iteration_time, 2)} seconds")
        
    # Average iterations by generation
    iterations_fitness_average = list(zip(*iterations_fitness))
    iterations_fitness_average = [round(sum(iteration)/len(iteration),0) for iteration in iterations_fitness_average]

    return iterations_fitness_average

# Experiments configuration
experiments = [# [50, 100, 0.9, 0.2, tournament_sel, scramble_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, scramble_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, scramble_mutation, multi_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, swap_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, swap_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, swap_mutation, multi_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, inversion_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, inversion_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, inversion_mutation, multi_point_xo, False, True, False]

               # [50, 100, 0.9, 0.2, roulette_selection, scramble_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, scramble_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, scramble_mutation, multi_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, swap_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, swap_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, swap_mutation, multi_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, inversion_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, inversion_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, inversion_mutation, multi_point_xo, False, True, False]

               # [50, 100, 0.9, 0.2, rank_selection, scramble_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, scramble_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, scramble_mutation, multi_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, swap_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, swap_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, swap_mutation, multi_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, inversion_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, inversion_mutation, single_point_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, inversion_mutation, multi_point_xo, False, True, False]

               # [50, 100, 0.9, 0.2, tournament_sel, scramble_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, swap_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, inversion_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, scramble_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, swap_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, inversion_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, scramble_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, swap_mutation, arithmetic_xo, False, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, inversion_mutation, arithmetic_xo, False, True, False]

               # [50, 100, 0.9, 0.2, tournament_sel, scramble_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, swap_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, tournament_sel, inversion_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, scramble_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, swap_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, roulette_selection, inversion_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, scramble_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, swap_mutation, arithmetic_xo, True, True, False],
               # [50, 100, 0.9, 0.2, rank_selection, inversion_mutation, arithmetic_xo, True, True, False]

               [50, 100, 0.8, 0.2, tournament_sel, scramble_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, tournament_sel, swap_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, tournament_sel, inversion_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, roulette_selection, scramble_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, roulette_selection, swap_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, roulette_selection, inversion_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, rank_selection, scramble_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, rank_selection, swap_mutation, arithmetic_xo, False, True, False],
               [50, 100, 0.8, 0.2, rank_selection, inversion_mutation, arithmetic_xo, False, True, False]
               ]

# List using the columns of the experiments list, this is done to make the code more readable
population_size = [exp[0] for exp in experiments]
generations = [exp[1] for exp in experiments]
crossover_probability = [exp[2] for exp in experiments]
mutation_probability = [exp[3] for exp in experiments]
selection = [exp[4].__name__ for exp in experiments]
mutation = [exp[5].__name__ for exp in experiments]
crossover = [exp[6].__name__ for exp in experiments]
elitism = [exp[7] for exp in experiments]
replacement = [exp[8] for exp in experiments]
slippery = [exp[9] for exp in experiments]

variable_list = [population_size, generations, crossover_probability, mutation_probability, 
                 selection, mutation, crossover, elitism, replacement, slippery]

selection_list = []
for variable in variable_list:
    if len(set(variable)) >= 2:
        selection_list.append(variable)

label_list = []
for l in range(len(selection_list[0])):
    label = ([v[l] for v in selection_list])
    label = " & ".join(label)
    label_list.append(label)
    
# Run the experiments
for exp in experiments:
    print(f"Running experiment: {experiments.index(exp) + 1}")
    fitness_experiments.append(run_experiment(population_size = exp[0],
                                              generations = exp[1],
                                              crossover_probability = exp[2],
                                              mutation_probability = exp[3],
                                              selection = exp[4],
                                              mutation = exp[5],
                                              crossover = exp[6],
                                              elitism = exp[7],
                                              replacement = exp[8],
                                              slippery = exp[9]))
    print(f"Experiment {experiments.index(exp) + 1} finished")
    print("--------------------------------------------------")

# Plot the fitness by experiment
for exp in fitness_experiments:
    plt.plot(exp)
    
plt.title("Fitness by Generation")
plt.xlabel("Generation") 
plt.ylabel("Fitness")
# Set the left and right margins
plt.subplots_adjust(left=0.08, right=0.73)
# Add a legend outside the plot
plt.legend(label_list, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# Show the plot
plt.show()

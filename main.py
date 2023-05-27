import time
import matplotlib.pyplot as plt
from charles import Population, Individual
from selection import roulette_selection, tournament_sel, rank_selection
from mutation import inversion_mutation, swap_mutation, scramble_mutation
from crossover import arithmetic_xo, single_point_co, mask_xo, uniform_xo, multi_point_crossover,heuristic_xo
from FL_fitness import get_fitness

# Individual Monkey Patching
Individual.get_fitness = get_fitness

fitness_experiments = []

def run_experiment(population_size, 
                   generations, 
                   crossover_probability, 
                   mutation_probability, 
                   selection, 
                   mutation, 
                   crossover, 
                   elitism, 
                   replacement, 
                   slippery,
                   sol_size=16,
                   valid_set=[0, 1, 2, 3]
                   ):

    iterations_fitness = []
    for i in range(200):
        start_time = time.time()
        
        # Create a population
        pop = Population(
            size=population_size,
            optim="max",
            sol_size=sol_size,
            valid_set=valid_set,
            replacement=replacement,
            slippery=slippery
        )

        # Evolve the population for 30 iterations
        iterations_fitness.append(pop.evolve(gens=generations, 
                                            xo_prob=crossover_probability, 
                                            mut_prob=mutation_probability, 
                                            select=selection,
                                            mutate=mutation, 
                                            crossover=crossover,
                                            elitism=elitism))
        
        end_time = time.time()  # Stop measuring the time
        iteration_time = end_time - start_time
        print(f"Iteration {i+1} time: {round(iteration_time,2)} seconds")
        
    # Average iterations by generation
    iterations_fitness_average = list(zip(*iterations_fitness))
    iterations_fitness_average = [round(sum(iteration)/len(iteration),0) for iteration in iterations_fitness_average]

    return iterations_fitness_average

# Experiments configuration
experiments = [
    [50,100,0.9,0.2,tournament_sel,inversion_mutation,heuristic_xo,False,True,False],
    [50,100,0.9,0.2,tournament_sel,inversion_mutation,arithmetic_xo,False,True,False],
    #[50,100,0.9,0.2,tournament_sel,inversion_mutation,uniform_xo,False,True,False],
    
    #[50,100,0.9,0.2,tournament_sel,swap_mutation,arithmetic_xo,False,True,False],
    #[50,100,0.9,0.2,tournament_sel,swap_mutation,single_point_co,False,True,False],
    #[50,100,0.9,0.2,tournament_sel,swap_mutation,uniform_xo,False,True,False],

    #[50,100,0.9,0.2,tournament_sel,scramble_mutation,arithmetic_xo,False,True,False],
    #[50,100,0.9,0.2,tournament_sel,scramble_mutation,single_point_co,False,True,False],
    #[50,100,0.9,0.2,tournament_sel,scramble_mutation,uniform_xo,False,True,False],
]

# create a list using the columns of the experiments list
# this is done to make the code more readable
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

# for each variable, find the unique values
variable_list = [population_size, generations, crossover_probability, mutation_probability, 
                 selection, mutation, crossover, elitism, replacement, slippery]

# find the first variable that has more than one unique value
selection_list = []
for variable in variable_list:
    if len(set(variable)) >= 2:
        selection_list.append(variable)

# 
label_list = []
for l in range(len(selection_list[0])):
    label = ([v[l] for v in selection_list])
    # create a string with the elements in the list
    label = "/".join(label)
    # insert label in a list
    label_list.append(label)
    


# Run the experiments
for exp in experiments:
    print(f"Running experiment: {experiments.index(exp)+1}")
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
    print(f"Experiment {experiments.index(exp)+1} finished")
    print("--------------------------------------------------")

# Plot the fitness by experiment
for exp in fitness_experiments:
    plt.plot(exp)
plt.xlabel("Generation") 
plt.ylabel("Fitness")
plt.title("Fitness by Generation")
# set the left and right margins
plt.subplots_adjust(left=0.08, right=0.73)
# add a legend
plt.legend([f"{label_list[i]}" for i in range(len(label_list))],bbox_to_anchor=(1, 0.5))
# show the plot
plt.show()


    
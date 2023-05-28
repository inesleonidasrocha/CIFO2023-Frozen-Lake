import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
    for i in range(100):
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
    iterations_fitness_gen = list(zip(*iterations_fitness))
    iterations_fitness_average = [int(round(sum(iteration)/len(iteration),0)) for iteration in iterations_fitness_gen]
    
    # Get the standard deviation of the iterations
    iterations_fitness_std = [int(round(np.std(iteration),0)) for iteration in iterations_fitness_gen]

    return iterations_fitness_average, iterations_fitness_std

# Experiments configuration
experiments = [
                [50, 100, 0.9, 0.2, roulette_selection, arithmetic_xo, scramble_mutation, True, True, True],
                [50, 100, 0.9, 0.2, tournament_sel, arithmetic_xo, scramble_mutation, True, True, False],
                [50, 100, 0.9, 0.2, rank_selection, arithmetic_xo, scramble_mutation, False, True, True],
               # [50, 100, 0.9, 0.2, rank_selection , arithmetic_xo, scramble_mutation, False, True, False]
               ]

# Check if there are experiments in the list
if len(experiments) == 0:
    raise Exception("You need to add experiments to the experiments list.")

# List using the columns of the experiments list, this is done to make the labels more readable
population_size = ["pop = " + str(exp[0]) for exp in experiments]
generations = ["gen = " + str(exp[1]) for exp in experiments]
crossover_probability = ["co = " + str(exp[2]) for exp in experiments]
mutation_probability = ["mut = " + str(exp[3]) for exp in experiments]
selection = [exp[4].__name__ for exp in experiments]
crossover = [exp[5].__name__ for exp in experiments]
mutation = [exp[6].__name__ for exp in experiments]
elitism = ["elite = " + str(exp[7]) for exp in experiments]
replacement = ["repl = " + str(exp[8]) for exp in experiments]
slippery = ["slip = " + str(exp[9]) for exp in experiments]

variable_list = [population_size, generations, crossover_probability, mutation_probability, 
                 selection, mutation, crossover, elitism, replacement, slippery]

selection_list = []
label_list = []
    
# Check if some variables in variable_list have different values in the experiments
if any(len(set(variable)) > 1 for variable in variable_list):
    for variable in variable_list:
        if len(set(variable)) >= 2:
            selection_list.append(variable)

    for l in range(len(selection_list[0])):
        label = ([v[l] for v in selection_list])
        label = " & ".join(label)
        label_list.append(label)
else:
    label_list = ["Experiment " + str(len(experiments))]

# Create the dataframe to save the results with two columns (Experiment and Fitness)
df_results = pd.DataFrame(columns = ["Experiment", "Fitness"])

# Run the experiments
for exp in experiments:
    print(f"Running experiment: {experiments.index(exp) + 1}")
    fitness_experiments.append(run_experiment(population_size = exp[0],
                                              generations = exp[1],
                                              crossover_probability = exp[2],
                                              mutation_probability = exp[3],
                                              selection = exp[4],
                                              crossover = exp[5],
                                              mutation = exp[6],
                                              elitism = exp[7],
                                              replacement = exp[8],
                                              slippery = exp[9]))
    # Calculate the overall fitness of the last generation of the experiment
    # and save it in the dataframe
    fitness_overall = int(round(np.mean(fitness_experiments[-1][0]),0))
    experiment = experiments.index(exp) + 1
    # Create a dictionary with the values
    new_data = pd.DataFrame({"Experiment": [experiment], "Fitness": [fitness_overall]})
    # Append the dictionary to the DataFrame
    df_results = pd.concat([df_results, new_data], ignore_index=True)
    print(f"Experiment {experiments.index(exp)+1} finished")
    print("--------------------------------------------------")
    
print(df_results)
    
'''# Plot the results
# Extract avg and std values from the fitness_experiments
avg = [exp[0] for exp in fitness_experiments]
std = [exp[1] for exp in fitness_experiments]

# Calculate the upper and lower bounds for the shaded area
upper_bound = [ [a + s for a, s in zip(avg[i], std[i])] for i in range(len(avg))]
lower_bound = [ [a - s for a, s in zip(avg[i], std[i])] for i in range(len(avg))]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the fitness by experiment
for a in range(len(avg)):
    # Plot the average line
    ax.plot(range(len(avg[a])), avg[a], label=label_list[a])
    # Fill the area between the bounds
    ax.fill_between(range(len(avg[a])), lower_bound[a], upper_bound[a], alpha=0.2)

# Set labels and title
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')
ax.set_title('Fitness Lanscape')

# Only display average line in the legend
#ax.legend(label_list,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:len(avg)], labels[:len(avg)], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# set the left and right margins
plt.subplots_adjust(left=0.08, right=0.73)

# Show the plot
plt.show()'''



# Plot the fitness by experiment

plt.subplots(figsize=(12, 6))

avg = [exp[0] for exp in fitness_experiments]

for exp in avg:
    plt.plot(exp)

plt.xlabel("Generation") 
plt.ylabel("Fitness")
plt.title("Fitness Lanscape")
# set the left and right margins
plt.subplots_adjust(left=0.08, right=0.6)
# Add a legend outside the plot
plt.legend(label_list, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
# show the plot
plt.show()

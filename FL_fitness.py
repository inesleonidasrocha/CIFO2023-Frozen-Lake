import gym

from charles import Population, Individual
'''from charles.selection import roulette_selection
from charles.mutation import inversion_mutation
from charles.crossover import pmx, cycle_xo, arithmetic_xo'''

def get_fitness(self, slippery):
    # Create the FrozenLake environment
    # Render mode is only for visualization purposes, so it can be removed
    # env = gym.make('FrozenLake-v1', render_mode="human", is_slippery=False)
    env = gym.make('FrozenLake-v1', is_slippery=slippery)
    
    # Set the initial state
    env.reset()

    # Define the actions mapping
    Hole = [5,7,11,12]
    Valid = [0,1,2,3,4,6,8,9,10,13,14]
    Goal = [15]

    # Punishment
    '''
    The maximum fitness if the agent got stuck in the same position
    without falling into a hole is 32 (16*2). So, the punishment if the agent 
    falls into a hole should be higher than 32.
    So, why not start the punishment at the last step at -33 and then decrease
    the punishment by 1 for each step?
    Also, the punishemnt should be higher if the agent falls into a hole
    in the first steps and lower if the agent falls into a hole in the last steps. 
    The punishment is calculated as follows:
    '''
    # print the results if you want to see the full punishment
    punishment = [-273 + 16 * i if i > 0 else 0 for i in range(len(self.representation))]  
    # print(punishment) 

    # Simulate the individual's actions in the environment
    fitness = 0  # Fitness score
    same_position = 0
    state = None
    status = None
    
    #######################################################################################################
    # Full round with no goal example
        # Never reaches the goal. The maximum fitness is -16.
    #self.representation = [2,2,0,0,2,2,0,0,2,2,0,0,2,2,0,0]
    # Same position example
        # In this one, the maximum fitness is -32. The agent got stuck in the same position
    #self.representation = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # Fall into a hole in the last step example
        # Here, the agent falls into a hole in the last step. The punishment is -33.
        # With this logic, the punishment where the agent falls into a hole in the last step
        # is bigger than the case where the agent runs out of steps.
    #self.representation = [2,0,2,0,2,0,2,0,2,0,2,0,2,0,2,1]
    #######################################################################################################
    
    # Loop through the individual's representation
    for action in range(len(self.representation)):
        new_state, _, done, _,_ = env.step(self.representation[action])
        if new_state in Hole:
            fitness = punishment[action]
            if same_position > 0:
                fitness = punishment[action] - same_position
            status = "Fail"
        elif new_state in Valid:           
            if state == None and new_state == 0:
                fitness -= 2
                same_position += 1
            elif state == new_state:
                fitness -= 2
                same_position += 1
            else:
                fitness -= 1
            state = new_state
        elif new_state in Goal:
            fitness += 0 # We don't need to add more fitness because the optimum fitness will be -5
            status = "Success"        

        # End the simulation when the game is over
        if done or len(self.representation) == action+1:
            #printings(done, self.representation, action, same_position, status, fitness, punishment)
            break

    return fitness

def printings(done, representation, action, same_position, status, fitness, punishment):
    # Print the details of each run
    if done or len(representation) == action+1:
        print("------------------------------------------------------------")
        print(f"Individual: {representation[:action+1]}")
        print(f"Total steps: {action+1}")
        if status == "Fail":
            print(f"Valid steps towards the goal: {action-same_position}")
            print(f"Number of times in the same position: {same_position}")
            print(f"Agent fell in a hole: 1")
            print(f"Punishement baseline: {punishment[action]}")
            print(f"Punishement fitness: {fitness}")
        elif status == "Success":
            print(f"Valid steps towards the goal: {action+1-same_position}")
            print(f"Number of times in the same position: {same_position}")
            print(f"Agent reaches the goal!")
            print(f"Success fitness: {fitness}")
        elif len(representation) == action+1:
            print(f"Valid steps towards the goal: {action+1-same_position}")
            print(f"Number of times in the same position: {same_position}")
            print(f"Agent ran out of steps!")
            print(f"Run-out fitness: {fitness}")
        print("------------------------------------------------------------")
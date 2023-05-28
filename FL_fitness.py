#import gym
import gymnasium as gym

from charles import Population, Individual

def get_fitness(self, slippery):
    
    # Render mode is only for visualization purposes, so it can be removed
    # env = gym.make('FrozenLake-v1', render_mode="human", is_slippery=False)
    
    # Create the FrozenLake environment
    env = gym.make('FrozenLake-v1', is_slippery=slippery)
    
    # Set the initial state
    env.reset()

    # Define the actions mapping
    Hole = [5,7,11,12]
    Valid = [0,1,2,3,4,6,8,9,10,13,14]
    Goal = [15]

    # Punishment
    punishment = [-273 + 16 * i if i > 0 else 0 for i in range(len(self.representation))]  

    # Simulate the individual's actions in the environment
    fitness = 0  # Fitness score
    same_position = 0
    state = None
    
    # Loop through the individual's representation
    for action in range(len(self.representation)):
        new_state, _, done, _,_ = env.step(self.representation[action])
        if new_state in Hole:
            fitness = punishment[action]
            if same_position > 0:
                fitness = punishment[action] - same_position
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

        # End the simulation when the game is over
        if done or len(self.representation) == action+1:
            break

    return fitness

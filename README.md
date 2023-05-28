<h1>FROZEN LAKE PROBLEM</h1>
 
 **COMPUTATIONAL INTELLIGENCE FOR OPTIMIZATION**
 
 Master in Data Science and Advanced Analytics<br>
 NOVA Information Management School<br>
 May, 2023
 

#### Contacts
Group 4:

Alex Santander, 20220658@novaims.unl.pt<br>
Carlota Carneiro, m20210684@novaims.unl.pt<br>
Inês Rocha, 20220052@novaims.unl.pt<br>
Susana Dias, 20220198@novaims.unl.pt


<h2>PROJECT DESCRIPTION</h2>

This project focuses on solving the Frozen Lake Problem (FLP) using Genetic Algorithm (GA) techniques. For the development of the project, we implemented and evaluated various selection, crossover, and mutation methods within the framework of GA for problem-solving. The main objective of this was to assess their performance, convergence, and effectiveness and compare their efficacy in achieving optimal solutions. 

The FLP is a classic grid-based navigation problem - see *gif* below - often used in reinforcement learning and artificial intelligence. It represents a scenario where an agent is situated on a frozen lake and needs to navigate to a goal location without falling into holes. The agent can take actions such as moving up, down, left, or right to transition between states. However, there are certain factors that add challenge to the problem:

* ``Slippery Ice:`` Some cells on the grid are covered in slippery ice, making the agent's movement less predictable. When the agent takes an action on a slippery ice cell, there is a chance that it will slide in a random direction instead of moving in the intended direction.

* ``Holes:`` Certain cells on the grid are marked as holes. If the agent steps into a hole, it falls through the ice and fails to reach the goal.

* ``Goal:`` There is a designated goal cell that the agent needs to reach in order to successfully solve the problem.

The objective of this problem is for the agent to find the optimal path from its starting position to the goal, while avoiding the holes. The Frozen Lake problem serves as a simple yet challenging environment to study and develop algorithms for navigation, decision-making, and learning in artificial intelligence.

![Alt Text](https://gymnasium.farama.org/_images/frozen_lake.gif)

<h3>Files:</h3>

_``charles.py``_  - Implementation of individuals and populations; facilitates the evolutionary process through selection, crossover, and mutation.<br>   

_``FL_fitness.py``_ - Defining the fitness function for the FLP using the Gym library.<br>

_``selection.py``_ - Implementation of selection algorithms: Tournament, Roulette and Rank.<br>

_``crossover.py``_ - Implementation of crossover algorithms: Arithmetic, Single Point, Multi-Point, Uniform, Uniform Mask and Heuristic.<br> 

_``mutation.py``_ - Implementation of mutation algorithms: Scramble, Swap and Inversion.<br>

_``main.py``_ - Applying various configurations of genetic algorithms to solve the FLP.


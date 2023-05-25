from random import randint, sample, uniform


def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2
    
def arithmetic_xo(p1, p2):
    """Implementation of arithmetic crossover/geometric crossover with constant alpha.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    alpha = uniform(0, 1)
    o1 = [None] * len(p1)
    o2 = [None] * len(p1)
    for i in range(len(p1)):
        o1[i] = int(round(p1[i] * alpha + (1-alpha) * p2[i],0))
        o2[i] = int(round(p2[i] * alpha + (1-alpha) * p1[i],0))
    return o1, o2

#---------------------------DOESN'T WORK YET ----------------------------
def cycle_xo(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # offspring placeholders
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)

    while None in offspring1:
        index = offspring1.index(None)
        val1 = p1[index]
        val2 = p2[index]

        # copy the cycle elements
        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        # copy the rest
        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    return offspring1, offspring2


def pmx(p1, p2):
    """Implementation of partially matched/mapped crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    xo_points = sample(range(len(p1)), 2)
    xo_points.sort()

    def pmx_offspring(x,y):
        o = [None] * len(x)
        print("------------------------------------------------------------")
        print(f"o = {o}")
        print(f"x's representation: {x.representation}, x's fitness : {x.fitness}")
        print(f"y's representation: {y.representation}, y's fitness : {y.fitness}")
        print(f"xo_points for sliding: {xo_points}")
        # offspring2
        print(f"o's slide: {o[xo_points[0]:xo_points[1]]}")
        o[xo_points[0]:xo_points[1]]  = x[xo_points[0]:xo_points[1]]
        print(f"x's slide: {x[xo_points[0]:xo_points[1]]}")
        print(f"y's slide: {y[xo_points[0]:xo_points[1]]}")

        z = set(y[xo_points[0]:xo_points[1]]) - set(x[xo_points[0]:xo_points[1]])
        print(f"Non duplicated values in y's slide: {set(y[xo_points[0]:xo_points[1]])}")
        print(f"Non duplicated values in x's slide: {set(x[xo_points[0]:xo_points[1]])}")
        print(f"Values contain in the y's slide but not in x's slide: {z}")
        
        # numbers that exist in the segment
        for i in z:    
            temp = i
            index = y.index(x[y.index(temp)])
            while o[index] is not None: # Infinite loop warning!!!!!
                temp = index
                index = y.index(x[temp])
                #break
                o[index] = i
            o[index] = i
            print(o)
            #print(y.representation)

        # numbers that doesn't exist in the segment
        while None in o:
            #print(f"Index: {o.index(None)}")
            index = o.index(None)
            o[index] = y[index]
            #print(o)
            #print(y.representation)
        return o

    o1, o2 = pmx_offspring(p1, p2), pmx_offspring(p2, p1)
    return o1, o2























from random import randint


def single_point_co(p1, p2):
    xo_point = randint(1,len(p1)-1)
    offspring1 = p1[:xo_point] + p2[xo_point:]
    offspring2 = p2[:xo_point] + p1[xo_point:]
    return offspring1,offspring2

if __name__ == '__main__':
    p1,p2 =[1,1,1,1], [0,0,0,0]
    o1,o2 = single_point_co(p1,p2)
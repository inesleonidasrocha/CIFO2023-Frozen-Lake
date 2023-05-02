from random import randint


def binary_mutation(individual):
    mut_index= randint(0,len(individual)-1)
    if individual[mut_index]==0:
        individual[mut_index]=1
    elif individual[mut_index]==1:
        individual[mut_index] = 0
    return individual


if __name__ == '__main__':
    test =[0,0,0,0]
    test = binary_mutation(test)
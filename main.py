import random

from PIL import Image
from scr.misc.helpers import *

def main(max):
    initPopulation(POPULATION_SIZE, GENERATIONS)
    spawnGeneration(GENERATIONS[0], MAZE, '0')
    GENERATIONS[0].sort(key=lambda x: x.fitness)

    #for ind in GENERATIONS[0]:
     #   print(ind)

    # print("======================")

    for iteration in range(1, max):
        GENERATIONS[iteration] = []

        createGeneration(GENERATIONS[iteration], GENERATIONS[iteration - 1], POPULATION_SIZE, iteration)
        spawnGeneration(GENERATIONS[iteration], MAZE, str(iteration))
        GENERATIONS[iteration].sort(key=lambda x: x.fitness)

        #for ind in GENERATIONS[iteration]:
            #print(ind)
       # print("======================")
    

if __name__ == "__main__":

    MAX_ITERATIONS = 30
    SIZE = 50
    MUTATION_FACTOR = 5
    GENERATIONS = {}
    POPULATION_SIZE = 100
    MAZE = Image.open('Laberintos/_Lab1.png').convert('RGB')

    main(MAX_ITERATIONS)

    
    
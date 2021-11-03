import random

from PIL import Image
from scr.misc.helpers import *

def main(max):
    initPopulation(POPULATION_SIZE, GENERATIONS)
    spawnGeneration(GENERATIONS[0], MAZE)
    # for ind in GENERATIONS[0]:
    #     MAZE.putpixel((ind.x_coordinate, ind.y_coordinate), (255, 0, 0))
    #     MAZE.save('Laberintos/output.png')
    #     ind.fitnessFunction(MAZE)

    for ind in GENERATIONS[0]:
        print(ind)

    print("======================")

    for iteration in range(1, max):
        GENERATIONS[iteration] = []

        while len(GENERATIONS[iteration]) < POPULATION_SIZE:
            father = random.choice(GENERATIONS[iteration - 1])
            mother = random.choice(GENERATIONS[iteration - 1])

            GENERATIONS[iteration] += [createOffspring(len(GENERATIONS[iteration]), father, mother, iteration)]

        for ind in GENERATIONS[iteration]:
            print(ind)
        print("======================")

        # for ind in GENERATIONS:
        #     x_coordinate = random.randint(0, 49)
        #     y_coordinate = random.randint(0, 49)
        #     population += [Individual(x, x_coordinate, y_coordinate)]
        #     MAZE.putpixel((x_coordinate, y_coordinate), (0, 0, 255))
        #     MAZE.save('Laberintos/output.png')
        # for ind in population:
        #     ind.fitnessFunction(image)
        #     print(ind)



    

if __name__ == "__main__":

    MAX_ITERATIONS = 10
    SIZE = 50
    MUTATION_FACTOR = 5
    GENERATIONS = {}
    POPULATION_SIZE = 10
    MAZE = Image.open('Laberintos/Lab1.png').convert('RGB')

    main(MAX_ITERATIONS)

    # main(MAX_ITERATIONS, mazeImg, first)
    # pickParents(mazeImg, first, gen1, 1, (255,0,0))
    # gen2 = []
    # pickParents(mazeImg, gen1, gen2, 2, (0,255,0))
    # gen3 = []
    # pickParents(mazeImg, gen2, gen3, 3, (0,255,255))

    
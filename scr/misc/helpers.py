import random

from ..classes.individual import Individual

def createOffspring(id, father, mother, gen):

    return Individual(id, father.x_coordinate, mother.y_coordinate, father, mother, gen)


def pickParents(image, gen1, gen2, genNum, color):
    for i in range(10):
        parent1 = random.choice(gen1)
        parent2 = random.choice(gen1)
        reproduce(parent1, parent2, gen2, i)

    for ind in gen2:
        image.putpixel((ind.x_coordinate, ind.y_coordinate), tuple(color))
        image.save('Laberintos/output' + str(genNum) + '.png')
        print(ind)

def initPopulation(maxIndividuals, gen):
    population = [Individual(i, random.randint(0, 49), random.randint(0, 49)) for i in range(maxIndividuals)]
    gen[0] = population

def spawnGeneration(indivList, maze):

    for ind in indivList:
        maze.putpixel((ind.x_coordinate, ind.y_coordinate), (255, 0, 0))
        maze.save('Laberintos/output.png')
        ind.fitnessFunction(maze)

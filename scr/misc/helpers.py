import random

from ..classes.individual import Individual

def createGeneration(population, ancesters, size, gen):

    population.sort(key=lambda x: x.fitness)

    while len(population) < size:
        father = random.choices(ancesters, weights=[i.fitness for i in ancesters])[0]
        mother = random.choices(ancesters, weights=[i.fitness for i in ancesters])[0]

        population += [Individual(len(population), father.x_coordinate, mother.y_coordinate, father, mother, gen)]


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

def spawnGeneration(indivList, maze, gen):

    for ind in indivList:
        maze.putpixel((ind.x_coordinate, ind.y_coordinate), (255, 0, 0))
        maze.save('Laberintos/generation'+gen+'.png')
        ind.fitnessFunction(maze)

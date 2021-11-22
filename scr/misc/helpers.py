import random
from PIL import Image

from ..classes.individual import Individual

def createGeneration(population, ancesters, size, gen):

    population.sort(key=lambda x: x.fitness)

    while len(population) < size:
        father = random.choices(ancesters, weights=[i.fitness for i in ancesters])[0]
        mother = random.choices(ancesters, weights=[i.fitness for i in ancesters])[0]

        geneX = geneCombiner(father.x_coordinate, mother.x_coordinate)
        geneY = geneCombiner(father.y_coordinate, mother.y_coordinate)


        population += [Individual(len(population), geneX, geneY, father, mother, gen)]

def geneCombiner(father, mother):

    maxLenght = len(max(f'{father:b}', f'{mother:b}'))

    geneFather = f'{father:0{maxLenght}b}'
    geneMother = f'{mother:0{maxLenght}b}'

    gene = ''
    switch = True
    while len(gene) < maxLenght:
        if switch:
            gene += geneFather[len(gene)]
            switch = False
        else:
            gene += geneMother[len(gene)]
            switch = True

    gene = int(gene, 2)

    if gene > 49:
        gene = 49
    elif gene < 0:
        gene = 0

    return gene

def pickParents(image, gen1, gen2, genNum, color):
    for i in range(10):
        parent1 = random.choice(gen1)
        parent2 = random.choice(gen1)
        reproduce(parent1, parent2, gen2, i)

    for ind in gen2:
        image.putpixel((ind.x_coordinate, ind.y_coordinate), tuple(color))
        image.save('Laberintos/output' + str(genNum) + '.png')
        #print(ind)

def initPopulation(maxIndividuals, gen):
    population = [Individual(i, random.randint(0, 49), random.randint(0, 49)) for i in range(maxIndividuals)]
    gen[0] = population

def spawnGeneration(indivList, maze, gen):
    maze = Image.open('Laberintos/_Lab1.png').convert('RGB')
    print("_----------GEN", gen)
    print(len(indivList))
    for ind in indivList:
        if(gen in ["0","10","16","22","29"]):
            #print("HERE")
            maze.putpixel((ind.x_coordinate, ind.y_coordinate), (255, 0, 0))
            maze.save('Laberintos/generation'+str(gen)+'.png')
        ind.fitnessFunction(maze)
        #if ind.fitness == 0:

            #maze.putpixel((ind.x_coordinate, ind.y_coordinate), (82, 82, 82))
            #maze.save('Laberintos/generation'+gen+'.png')

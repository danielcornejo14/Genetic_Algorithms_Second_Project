import random
from PIL import Image
#from natsort import natsorted
import os

from ..classes.individual import Individual


RUTA_LABERINTO = 'Laberintos/_Lab2.png'

def arrayToNumber(array):
    number = 0
    potencia = 1
    for i in reversed(array):
        number += int(i)*potencia
        potencia = potencia*2


    return number
"""
def walkLaberint(array):
    for root, dirs, files in os.walk('Laberintos'):

        for file_name in natsorted(files, key=lambda x: x.lower()):
            rel_file = os.path.join('Laberintos', file_name)
            print(rel_file)
            array.append(rel_file)"""

"""REPRODUCTION FUNCTIONS"""
def getChromosome(number):
    #6 por 6 bits necesarios
    dnaArray = [0]*6
    binary = bin(number)
    largo = len(binary)
    #borrar 0b
    shortBinary = binary[2:largo]
    n = len(dnaArray)-1
    for i in reversed(shortBinary):
        dnaArray[n]=int(i)
        n-=1

    return dnaArray

def mutate(dnaChild):

    indexes = []
    x = arrayToNumber(dnaChild[:6])
    y = arrayToNumber(dnaChild[-6:])
    mutate = random.randint(1,100)
    if(mutate<8):
        displacement = random.randint(1, 5)
        direction = random.choice([-1, 1])
        coordinate = random.choice([0, 1])
        if coordinate == 0:
            x += (displacement * direction)
            if x>= 49:
                x = 49
            if x< 0:
                x = 0
        elif coordinate == 1:
            y += (displacement * direction)
            if y >= 49:
                y = 49
            if y< 0:
                y = 0

    dnaChild = getChromosome(x)+getChromosome(y)
    return dnaChild

def getDnaChild(father,mother):
    """
    Make 2 childs from parents
    """
    #Chromosome size 12
    dnaFather = getChromosome(father.x_coordinate)+getChromosome(father.y_coordinate)
    dnaMother = getChromosome(mother.x_coordinate)+getChromosome(mother.y_coordinate)

    cutPoint = random.randint(3,9)


    dnaChild = dnaFather[0:cutPoint]+dnaMother[cutPoint:len(dnaMother)]
    dnaChild2 = dnaMother[0:cutPoint]+dnaFather[cutPoint:len(dnaFather)]

    dnaChild = mutate(dnaChild)
    dnaChild2 = mutate(dnaChild2)
    
    childs = [dnaChild, dnaChild2]
    return childs

def makePool(population):
    pool = []
    for ind in population:
        for i in range(ind.fitness):
            pool.append(ind)
    return pool


""" GENERATION FUNCTIONS """
def createGeneration(population, ancesters, size, gen):

    #population
    pool = makePool(ancesters)
    #ancesters.sort(key=lambda x: x.fitness)

    porcentaje = int(len(ancesters)*0.15)

    #Se mantiene el 15% de los mejores ancestros
    population += ancesters[:porcentaje]

    while len(population) < size:
        #Choose 2 parents for the childs in the pool
        number1 = random.randint(0,len(pool)-1)
        father = pool[number1]
        number2 = random.randint(0,len(pool)-1)
        mother = pool[number2]

        #Result of the mix
        result = getDnaChild(father, mother)

        #getDnaChild returns 2 individuals
        dnaChild =result[0]
        dnaChild2 = result[1]

        geneX = arrayToNumber(dnaChild[:6])
        geneY = arrayToNumber(dnaChild[-6:])

        geneX2 = arrayToNumber(dnaChild2[:6])
        geneY2 = arrayToNumber(dnaChild2[-6:])

        population += [Individual(str(gen)+"-"+str(len(population)), geneX, geneY, father, mother, gen)]
        population += [Individual(str(gen)+"-"+str(len(population)+1), geneX2, geneY2, father, mother, gen)]

def initPopulation(maxIndividuals, gen):
    """
    Create the first generation
    """
    population = [Individual("0-"+str(i), random.randint(0, 49), random.randint(0, 49)) for i in range(maxIndividuals)]
    gen[0] = population

def spawnGeneration(indivList, path, gen):
    """
    Put individuals in the output image, also calculates the fitness
    """
    fails = 0
    maze = Image.open(RUTA_LABERINTO).convert('RGB')
    print("----------GENERATION", gen)
    promedio = 0
    string = ""
    for ind in indivList:
        try:
            ind.fitnessFunction(maze)
            promedio += ind.fitness
            string += ind.toString()
            if int(gen) < 15 or int(gen) > 30:
                maze.putpixel((ind.x_coordinate, ind.y_coordinate), (255, 0, 0))
                maze.save('Laberintos/gen'+str(gen)+'.png')
        except:
            fails += 1
    
    #print("FAILS ", fails)
    string+="-\n"
    file = open("GENERATIONS.txt", "a")
    file.write(string)
    file.close()
    promedio = promedio / len(indivList)
    print("Promedio fitness ", promedio)

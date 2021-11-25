import os
os.system('cmd /c "java mian.java"')
from PIL import Image


import random
from scr.misc.helpers import *

def main(max):

    initPopulation(POPULATION_SIZE, GENERATIONS)
    spawnGeneration(GENERATIONS[0], RUTA_LABERINTO, '0')
    #Se ordena por fitness de mayor a menor
    GENERATIONS[0].sort(key=lambda x: x.fitness, reverse=True)
    for iteration in range(1, max):
        GENERATIONS[iteration] = []

        createGeneration(GENERATIONS[iteration], GENERATIONS[iteration-1], POPULATION_SIZE, iteration)
        #Se ordena por fitness de mayor a menor
        GENERATIONS[iteration].sort(key=lambda x: x.fitness, reverse=True)
        spawnGeneration(GENERATIONS[iteration], MAZE, str(iteration))


        
        
       
    

if __name__ == "__main__":

    MAX_ITERATIONS = 16
    GENERATIONS = {}
    POPULATION_SIZE = 400

    # main(MAX_ITERATIONS)

    ImageList = []

    #walkLaberint(ImageList)
    MAZE = Image.open(RUTA_LABERINTO).convert('RGB')
    
    
    file = open("GENERATIONS.txt", "w")
    file.write("")
    file.close()

    file = open("GENERATIONS.txt", "a")
    file.write(RUTA_LABERINTO+"\n")
    file.close()
    main(MAX_ITERATIONS)
    os.system('cmd /c "java mian.java"')
    
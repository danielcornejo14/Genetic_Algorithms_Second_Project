import random

from PIL import Image
from scr.classes.individual import Individual

#function to open and read the maze
def readMaze(mazeNumber, maze):
    mazeImg = Image.open('Laberintos/Lab'+str(mazeNumber)+'.png').convert('RGB')
    for i in range(SIZE):
        holder = []
        for j in range(SIZE):
            holder.append(mazeImg.getpixel((j, i)))
        maze.append(holder)

def printMaze(maze):
    for y in maze:
        print(y)

def main(maxIterations, image):

    for iteration in range(maxIterations):
        population = []
        for x in range(10):
            population += [Individual(x, random.randint(0, 49), random.randint(0, 49))]

        for ind in population:
            ind.fitnessFunction(image)
            print(ind)
        return



if __name__ == "__main__":
    MAX_ITERATIONS = 1000
    SIZE = 50
    mazeImg = Image.open('Laberintos/Lab1.png').convert('RGB')
    main(MAX_ITERATIONS, mazeImg)
    

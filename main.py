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

def main(maxIterations, image, population):
    for iteration in range(maxIterations):
        for x in range(10):

            x_coordinate=random.randint(0, 49)
            y_coordinate=random.randint(0, 49)
            population += [Individual(x, x_coordinate, y_coordinate)]
            image.putpixel((x_coordinate, y_coordinate), (0,0,255))
            image.save('Laberintos/output.png')
        for ind in population:
            ind.fitnessFunction(image)
            #print(ind)
        return

#Maybe this should be moved to another part of the program, meanwhile is here
def reproduce(father,mother, gen, n):
    x = father.getMutationX()
    y = mother.getMutationY()
    ind = Individual(n, x, y)
    ind.setFather = father
    ind.setMother = mother
    gen.append(ind)

#Maybe this should be moved to another part of the program, meanwhile is here
def pickParents(image, gen1, gen2, genNum, color):
    for i in range(10):
        parent1=random.choice(gen1) 
        parent2=random.choice(gen1)
        reproduce(parent1, parent2, gen2, i)

    for ind in gen2:
        image.putpixel((ind.x_coordinate, ind.y_coordinate), tuple(color))
        image.save('Laberintos/output'+str(genNum)+'.png')
        print(ind) 
    
    

if __name__ == "__main__":
    MAX_ITERATIONS = 1000
    SIZE = 50
    mazeImg = Image.open('Laberintos/Lab1.png').convert('RGB')
    
    first = []
    gen1 = []
    main(MAX_ITERATIONS, mazeImg, first)
    pickParents(mazeImg, first, gen1, 1, (255,0,0))
    gen2 = []
    pickParents(mazeImg, gen1, gen2, 2, (0,255,0))
    gen3 = []
    pickParents(mazeImg, gen2, gen3, 3, (0,255,255))

    
from scr.GUI.testGUI import mainApp
import tkinter as tk
import os

from PIL import Image
from scr.misc.helpers import *

def main(max):
    initPopulation(POPULATION_SIZE, GENERATIONS)
    spawnGeneration(GENERATIONS[0], MAZE, '0')
    GENERATIONS[0].sort(key=lambda x: x.fitness)

    for ind in GENERATIONS[0]:
        print(ind)

    # print("======================")

    for iteration in range(1, max):
        GENERATIONS[iteration] = []

        createGeneration(GENERATIONS[iteration], GENERATIONS[iteration - 1], POPULATION_SIZE, iteration)
        spawnGeneration(GENERATIONS[iteration], MAZE, str(iteration))
        GENERATIONS[iteration].sort(key=lambda x: x.fitness)

        for ind in GENERATIONS[iteration]:
            print(ind)
        print("======================")
    

if __name__ == "__main__":

    MAX_ITERATIONS = 10
    SIZE = 50
    MUTATION_FACTOR = 5
    GENERATIONS = {}
    POPULATION_SIZE = 200
    MAZE = Image.open('Laberintos/_Lab1.png').convert('RGB')

    ImageList = []

    for root, dirs, files in os.walk('Laberintos'):
        for file_name in sorted(files, key=int):
            rel_dir = os.path.relpath(root, '.')
            rel_file = os.path.join(rel_dir, file_name)
            rel_file.replace('\\', '/')
            print(rel_file)
            ImageList.append(rel_file)

    print(ImageList)
    # for x in ImageList[0:3]:
    #     Image.open(x).show()

    # root = tk.Tk()
    # mainApp(root, )
    # root.mainloop()

    #main(MAX_ITERATIONS)


    
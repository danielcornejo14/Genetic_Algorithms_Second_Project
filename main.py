from PIL import Image

from scr.misc.helpers import *

def main(max):

    initPopulation(POPULATION_SIZE, GENERATIONS)
    spawnGeneration(GENERATIONS[0], 'Laberintos/_Lab7.png', '0')
    #Se ordena por fitness de mayor a menor
    GENERATIONS[0].sort(key=lambda x: x.fitness, reverse=True)

    for iteration in range(1, max):
        GENERATIONS[iteration] = []

        createGeneration(GENERATIONS[iteration], GENERATIONS[iteration-1], POPULATION_SIZE, iteration)

        #Se ordena por fitness de mayor a menor
        GENERATIONS[iteration].sort(key=lambda x: x.fitness, reverse=True)

        spawnGeneration(GENERATIONS[iteration], MAZE, str(iteration))
        
    

if __name__ == "__main__":

    MAX_ITERATIONS = 41
    SIZE = 50
    MUTATION_FACTOR = 5
    GENERATIONS = {}
    POPULATION_SIZE = 500
    MAZE = Image.open('Laberintos/_Lab7.png').convert('RGB')

    # main(MAX_ITERATIONS)

    ImageList = []

    walkLaberint(ImageList)

    print(ImageList)
    # for x in ImageList[0:3]:
    #     Image.open(x).show()

    # root = tk.Tk()
    # mainApp(root, )
    # root.mainloop()



    
    
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

if __name__ == "__main__":
    mazeNumber = 1
    mainMaze = []
    SIZE = 50

    readMaze(mazeNumber, mainMaze)
    printMaze(mainMaze)

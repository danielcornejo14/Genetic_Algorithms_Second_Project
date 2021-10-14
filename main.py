from PIL import Image
from scr.classes.pixel import Pixel


if __name__ == "__main__":
    mainMaze = []
    SIZE = 50

    maze = Image.open('Laberintos/Lab1.png').convert('RGB')
    for i in range(SIZE):
        holder = []
        for j in range(SIZE):
            holder.append(Pixel(i, j, maze.getpixel((i,j))))
        mainMaze.append(holder)

    for i in mainMaze:
        holder = []
        for j in i:
            holder += [j.value]
        print(holder)
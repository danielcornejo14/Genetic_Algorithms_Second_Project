import random
from PIL import Image

IMAGESIZE = 50
PIXELSNUMBER = 5

class Individual:
    #Parameters (in development)
    id: int
    x_coordinate: int
    y_coordinate: int
    fitness: int
    father: None
    mother: None
    generation: int


    def __init__(self, id, x, y, father=None, mother=None, generation=0):
        """
        Inicialization function
        :param int id: object identificator
        :param int x: the x coordinate on the image where the individual resides
        :param int y: the y coordinate on the image where the individual resides
        :param Individual or None father: the father of the current read individual
        :param Individual or None mother: the mother of the current read individual
        :param int generation: the number of the generation to which the current indiviadual belongs

        :return:
        """
        self.id = id
        self.x_coordinate = x
        self.y_coordinate = y
        self.fitness = 0
        self.father = father
        self.mother = mother
        self.generation = generation
    
    def __getPixelSum(self, pixel):
        if pixel == (82, 82, 82):
            return 0
        elif pixel == (255, 0, 0):
            return 10
        elif pixel == (0, 255, 0) or pixel == (0, 0, 255):
            return 255 * 3
        else:
            return pixel[0]+pixel[1]+pixel[2]

    def __evaluateUp(self, image):
        y = self.y_coordinate - 1 
        count = 0
        while(y >= 0 and count < PIXELSNUMBER):
            self.fitness += self.__getPixelSum(image.getpixel((self.x_coordinate, y))) 
            y -= 1
            count += 1
            

    def __evaluateDown(self, image):
        y = self.y_coordinate + 1 
        count = 0
        while(y < IMAGESIZE and count < PIXELSNUMBER):
            self.fitness += self.__getPixelSum(image.getpixel((self.x_coordinate, y)))
            y += 1
            count += 1

    def __evaluateRight(self, image):
        x = self.x_coordinate + 1 
        count = 0
        while(x < IMAGESIZE and count < PIXELSNUMBER):
            self.fitness += self.__getPixelSum(image.getpixel((x, self.y_coordinate)))
            x += 1
            count += 1

    def __evaluateLeft(self,image): 
        x = self.x_coordinate -1 
        count = 0
        while(x >= 0 and count < PIXELSNUMBER):
            self.fitness += self.__getPixelSum(image.getpixel((x, self.y_coordinate)))
            x -= 1
            count += 1

    def fitnessFunction(self, image):
        self.__evaluateUp(image)
        self.__evaluateDown(image)
        self.__evaluateRight(image)
        self.__evaluateLeft(image)

    def getMutationX(self):
        leftLimit = 5 if self.x_coordinate > 5 else self.x_coordinate
        rightLimit = IMAGESIZE - self.x_coordinate - 1
        rigthLimit = 5 if rightLimit > 4 else rightLimit

        placement = random.randint(0,rigthLimit)-leftLimit

        return self.x_coordinate+placement

    def getMutationY(self):
        downLimit = IMAGESIZE - self.y_coordinate - 1
        upLimit = 5 if self.y_coordinate > 5 else self.y_coordinate
        downLimit = 5 if downLimit > 4 else downLimit

        placement = random.randint(0,downLimit)-upLimit

        return self.y_coordinate + placement

    def mutate(self):
        """
        selects random number from 1 to 5, then is multiplied randomly with 1, or -1 to select a direction, finally the
        X or Y coordinate is selected randomly in order to add the displacement
        :return:
        """

        displacement = random.randint(1, 5)
        direction = random.choice([-1, 1])
        coordinate = random.choice([0, 1])

        if coordinate == 0:
            self.x_coordinate += (displacement * direction)
            if self.x_coordinate > 50:
                self.x_coordinate = 50
            if self.x_coordinate < 0:
                self.x_coordinate = 0
        elif coordinate == 1:
            self.y_coordinate += (displacement * direction)
            if self.y_coordinate > 50:
                self.y_coordinate = 50
            if self.y_coordinate < 0:
                self.y_coordinate = 0


    def __repr__(self):
        """
        Overwrites the object representation

        :return:
        """
        return "id: {} | fitness: {} | generation: {} | coordinates: ({},{}) | parents id: F {} : M {}".format(self.id,
                                                                                                           self.fitness,
                                                                                                           self.generation,
                                                                                                           self.x_coordinate,
                                                                                                           self.y_coordinate,
                                                                                                           self.father.id if self.father is not None else 'null',
                                                                                                           self.mother.id if self.father is not None else 'null')

    

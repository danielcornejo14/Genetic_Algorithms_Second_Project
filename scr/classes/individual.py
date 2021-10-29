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


    def __repr__(self):
        """
        Overwrites the object representation

        :return:
        """
        return "id: {} | fitness: {} | generation: {} | coordinates: ({},{})".format(self.id, self.fitness, self.generation, self.x_coordinate, self.y_coordinate)

    

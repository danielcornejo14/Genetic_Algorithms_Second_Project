import random
from PIL import Image
IMAGESIZE = 50
PIXELSNUMBER = 7

class Individual:
    #Parameters (in development)
    id: str
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
        if(pixel[0]<20 and pixel[1]<20 and pixel[2]<20):
            return -1
        else:
            return 20

    def __getPixels(self, x, y, image):
        """
        Return the pixel, if it exits the image return a black pixel
        """
        try:
            return image.getpixel((x,y))
        except IndexError:
            return (0,0,0) 

    def fitnessFunction(self, image):
        """
        Calculate the fitness of the individual
        More white pixels increment the fitness
        Black pixels reduce the fitness a bit

        The more walls the more the fitness get decreased
        """
        #Start with this number so the fitness don't become negative
        self.fitness=50

        #Walls
        p1,p2,p3,p4 = 0,0,0,0

        #Evaluate 4 directions
        #Left
        for i in range(1,PIXELSNUMBER):
            pixel = self.__getPixels(self.x_coordinate-i, self.y_coordinate, image)
            resultado = self.__getPixelSum(pixel)
            self.fitness += resultado
            if(resultado<0):
                p1 = 1
      
        #Right
        for i in range(1,PIXELSNUMBER):
            pixel = self.__getPixels(self.x_coordinate+i, self.y_coordinate, image)
            resultado = self.__getPixelSum(pixel)
            self.fitness += resultado
            if(resultado<0):
                p2 = 1
        #Up
        for i in range(1,PIXELSNUMBER):
            pixel = self.__getPixels(self.x_coordinate, self.y_coordinate-i, image)
            resultado = self.__getPixelSum(pixel)
            self.fitness += resultado
            if(resultado<0):
                p3 = 1
        #Down
        for i in range(1,PIXELSNUMBER):
            pixel = self.__getPixels(self.x_coordinate, self.y_coordinate+i, image)
            resultado = self.__getPixelSum(pixel)
            self.fitness += resultado
            if(resultado<0):
                p4 = 0.1

        #The less walls the less the fitness get affected
        prioridad = p1+p2+p3+p4
        self.fitness = int(self.fitness*1/prioridad)

        if(self.fitness <= 0):
            self.fitness = 1

    def toString(self):
        salida = ""
        salida += str(self.id)+";"+str(self.fitness)+";"+str(self.generation)+";"+str(self.x_coordinate)+";"+str(self.y_coordinate)+";"

        if(self.father == None or self.mother == None):
            salida += "null"+";"+"null"
        else:
            salida += str(self.father.id)+";"+str(self.mother.id)

        return salida+"\n"
    
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

    

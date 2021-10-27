class Individual:
    #Parameters (in development)
    id: int
    x_coordinate: int
    y_coordinate: int
    fitness: int
    father: None
    mother: None
    generation: int


    def __init__(self, x, y, father=None, mother=None, generation=0):
        """
        Inicialization function
        :param int x: the x coordinate on the image where the individual resides
        :param int y: the y coordinate on the image where the individual resides
        :param Individual or None father: the father of the current read individual
        :param Individual or None mother: the mother of the current read individual
        :param int generation: the number of the generation to which the current indiviadual belongs

        :return:
        """
        self.x_coordinate = x
        self.y_coordinate = y
        self.fitness = 0
        self.father = father
        self.mother = mother
        self.generation = generation

    def __repr__(self):
        """
        Overwrites the object representation

        :return:
        """
        return "id: {} | fitness: {} | generation: {}".format(self.id, self.fitness, self.generation)

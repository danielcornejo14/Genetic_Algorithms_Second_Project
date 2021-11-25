
public class Individual{
	public int x;
	public int y;
	public int fitness;
	public int generation;
	public String id;
	public String father;
	public String mother;
	public Individual(int x, int y, int fitness, int generation, String id, String father, String mother){
		this.x=x;
		this.y=y;
		this.fitness=fitness;
		this.generation=generation;
		this.id=id;
		this.father=father;
		this.mother=mother;
	}
	public Individual(){
		
	}
	public String getData(){
		String salida="";
		
		salida+=this.id+";";
		salida+=String.valueOf(this.fitness)+";";
		salida+=String.valueOf(this.generation)+";";
		salida+=String.valueOf(this.x)+";";
		salida+=String.valueOf(this.y)+";";
		salida+=this.father+";";
		salida+=this.mother+";";
		return salida;
	}

    public int getFitness() {
        return fitness;
    }

    public void setFitness(int fitness) {
        this.fitness = fitness;
    }

    public int getGeneration() {
        return generation;
    }

    public void setGeneration(int generation) {
        this.generation = generation;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getFather() {
        return father;
    }

    public void setFather(String father) {
        this.father = father;
    }

    public String getMother() {
        return mother;
    }

    public void setMother(String mother) {
        this.mother = mother;
    }
	public int getX(){
		return this.x;
	}
	public int getY(){
		return this.y;
	}
}
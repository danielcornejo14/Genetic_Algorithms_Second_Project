    
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.awt.image.BufferedImage;

import java.io.*;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.HashMap;
import static javax.swing.ScrollPaneConstants.*;

class Formulario extends JFrame{
    public int GENERACIONES = 15;
	public int genActual;
    public HashMap<String,HashMap<String, Individual>> generations; 
    public HashMap<String, Individual>individuals;
    public JButton[][] botones;
    public JLabel ind,fit,posX,posY,padre,madre,gen,indM,fitM,posXM,posYM,genM,indP,fitP,posXP,posYP,genP, lblGen;
    public JButton btnAtras,btnAdelante;
    BufferedImage image;
    int width;
    int height;
    String RUTA;
    File input;

    public Formulario() {
        genActual=0;
        cargarArchivo();
    	
    	botones = new JButton[50][50];
        setLayout(null);
        input = new File(RUTA);
        try{
            image = ImageIO.read(input);
            width = image.getWidth();
            height = image.getHeight();

        }catch(Exception e){

        }
        crearBotones();
         //LABELS INFO INDIVIDUO
         ind = new JLabel("ID: "); 
         ind.setBounds(650,50,100,20);
         fit = new JLabel("Fitness: ");
         fit.setBounds(750,50,100,20);
         posX = new JLabel("X: ");
         posX.setBounds(650,90,100,20);
         posY = new JLabel("Y: ");
         posY.setBounds(750,90,100,20);
         padre = new JLabel("ID Padre: ");
         padre.setBounds(650, 130,100,20);
         madre = new JLabel("ID Madre: ");
         madre.setBounds(750,130,100,20);
         gen = new JLabel("Generacion: ");
         gen.setBounds(650,170,100,20);
         add(ind);
         add(fit);
         add(posX);
         add(posY);
         add(padre);
         add(madre);

         //LABELS MADRE Y PADRE 
         JLabel madre = new JLabel("Madre: ");
         madre.setBounds(650,225,100,20);
         indM = new JLabel("ID: "); 
         indM.setBounds(650,240,100,20);
         fitM = new JLabel("Fitness: ");
         fitM.setBounds(750,240,100,20);
         posXM = new JLabel("X: ");
         posXM.setBounds(650,280,100,20);
         posYM = new JLabel("Y: ");
         posYM.setBounds(750,280,100,20);
         genM = new JLabel("Generacion: ");
         genM.setBounds(650,320,100,20);

         JLabel padre = new JLabel("Padre: ");
         padre.setBounds(850,225,100,20);
         indP = new JLabel("ID: "); 
         indP.setBounds(850,240,100,20);
         fitP = new JLabel("Fitness: ");
         fitP.setBounds(950,240,100,20);
         posXP = new JLabel("X: ");
         posXP.setBounds(850,280,100,20);
         posYP = new JLabel("Y: ");
         posYP.setBounds(950,280,100,20);
         genP = new JLabel("Generacion: ");
         genP.setBounds(850,320,100,20);

         add(padre);
         add(madre);
         add(indM);
         add(fitM);
         add(posXM);
         add(posYM);
         add(indP);
         add(fitP);
         add(posXP);
         add(posYP);
         add(genP);
         add(genM);

         //Label generacion
         lblGen = new JLabel("GENERACION: 0");
         lblGen.setBounds(760, 415, 150,40);

         add(lblGen);

         //Botones
         btnAtras = new JButton("<<");
         btnAtras.setBounds(675, 415, 65,35);
         btnAdelante = new JButton(">>");
         btnAdelante.setBounds(875, 415, 65,35);

         btnAdelante.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    siguienteGeneracion();
                }
            });
         btnAtras.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    anteriorGeneracion();
                }
            });
      	add(btnAtras);
        add(btnAdelante);

        setBotones(generations.get("0"));


        
        //boton1.addActionListener(this);
    }
    public void crearBotones(){
        try {
            int count = 0;
            int x = 50;
            int y = 50;
            
            for(int i=0; i<height; i++) {           
               for(int j=0; j<width; j++) {
                Color c = new Color(image.getRGB(j, i));
                    JButton boton1=new JButton();
                    boton1.setBounds(x,y,10,10);
                    botones[i][j]=boton1;
                    boton1.setBackground(new java.awt.Color(c.getRed(),c.getGreen(),c.getBlue()));
                    boton1.setActionCommand("");
                    x+=10;
                    add(boton1);
               }
               y+=10;
               x=50;
         }

      } catch (Exception e) {}

    }
    public void limpiarBotones(){
        for(int i=0; i<height; i++) {           
               for(int j=0; j<width; j++) {
                    Color c = new Color(image.getRGB(j, i));
                    JButton boton1=botones[i][j];
                    boton1.setBackground(new java.awt.Color(c.getRed(),c.getGreen(),c.getBlue()));
                    boton1.setActionCommand("");
               }
         
        }
    }

    public void setBotones(HashMap<String, Individual>individuals){
        limpiarBotones();
    	for (HashMap.Entry<String, Individual> entry : individuals.entrySet()) {
            
            try{
            int x = entry.getValue().getX();
            int y = entry.getValue().getY();
            botones[y][x].setBackground(new java.awt.Color(255,0,0));
            botones[y][x].setActionCommand(entry.getValue().getId());
            botones[y][x].addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent evt) {
                    mostrarContenido(evt);
                }
            });

            }catch(Exception e ){

            }

    	}
    }
    public void cargarArchivo(){
    	generations = new HashMap<String,HashMap<String, Individual>>();
    	individuals = new HashMap<String, Individual>();
    	BufferedReader reader;
		try {
			reader = new BufferedReader(new FileReader(
					"GENERATIONS.txt"));
			String line = reader.readLine();
            RUTA = line;
            line = reader.readLine();
			while (line != null) {
        		String[] v = line.split(";");
        		Individual i = new Individual(Integer.parseInt(v[3]), Integer.parseInt(v[4]), Integer.parseInt(v[1]),Integer.parseInt(v[2]), v[0] ,v[5], v[6]);
        		individuals.put(v[0], i);
            
				// read next line
				line = reader.readLine();
				if(line.equals("-")){
					generations.put(v[2], individuals);
					individuals = new HashMap<String, Individual>();
					line = reader.readLine();
				}
			}
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}


    }
    public void siguienteGeneracion(){
        genActual++;
        if(genActual>GENERACIONES){
            genActual=0;
        }

        setBotones(generations.get(String.valueOf(genActual)));
        lblGen.setText("GENERACION: "+String.valueOf(genActual));
    }
    public void anteriorGeneracion(){
        genActual--;

        if(genActual<0){
            genActual=GENERACIONES;
        }

        setBotones(generations.get(String.valueOf(genActual)));
        lblGen.setText("GENERACION: "+String.valueOf(genActual));
    }
    public Individual buscarIndividuo(String id){
        if(id.equals("null")){
            return new Individual();

        }else{
             String[] gen = id.split("-");
            Individual i = generations.get(gen[0]).get(id);
            return i;
        }
       
    }

    public void mostrarContenido(java.awt.event.ActionEvent evt){

    	String id = evt.getActionCommand();
        Individual i = buscarIndividuo(id);
    	ind.setText("ID: "+id);
    	fit.setText("Fitness: "+String.valueOf(i.getFitness()));
    	posX.setText("X: "+String.valueOf(i.getX()));
    	posY.setText("Y: "+String.valueOf(i.getY()));
    	padre.setText("ID Padre: "+i.getFather());
    	madre.setText("ID Madre: "+i.getMother());
    	gen.setText("Generacion: "+String.valueOf(i.getGeneration()));

        llenarPadres(i.getFather(),i.getMother());
    	
    }

    public void llenarPadres(String padre, String madre){
    	Individual iPadre = buscarIndividuo(padre);
        Individual iMadre = buscarIndividuo(madre);

    	indP.setText("ID: "+iPadre.getId());
    	fitP.setText("Fitness: "+String.valueOf(iPadre.getFitness()));
    	posXP.setText("X: "+String.valueOf(iPadre.getX()));
    	posYP.setText("Y: "+String.valueOf(iPadre.getX()));
    	genP.setText("Generacion: "+String.valueOf(iPadre.getGeneration()));

        indM.setText("ID: "+iMadre.getId());
        fitM.setText("Fitness: "+String.valueOf(iMadre.getFitness()));
        posXM.setText("X: "+String.valueOf(iMadre.getX()));
        posYM.setText("Y: "+String.valueOf(iMadre.getX()));
        genM.setText("Generacion: "+String.valueOf(iMadre.getGeneration()));

    }
    
    
    public static void main(String[] ar) {
        Formulario formulario1=new Formulario();
        formulario1.setBounds(0,0,1200,600);
        formulario1.setVisible(true);
        formulario1.setTitle("Visualizacion");
        formulario1.setLocationRelativeTo(null);
        formulario1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		//formulario1.setBotones(formulario1.generations.get("14"));

       
		
    }
}


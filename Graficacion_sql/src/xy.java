/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author horacio
 */
import java.awt.Color; 
import java.awt.BasicStroke; 

import org.jfree.chart.ChartPanel; 
import org.jfree.chart.JFreeChart; 
import org.jfree.data.xy.XYDataset; 
import org.jfree.data.xy.XYSeries; 
import org.jfree.ui.ApplicationFrame; 
import org.jfree.ui.RefineryUtilities; 
import org.jfree.chart.plot.XYPlot; 
import org.jfree.chart.ChartFactory; 
import org.jfree.chart.plot.PlotOrientation; 
import org.jfree.data.xy.XYSeriesCollection; 
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;

public class xy extends ApplicationFrame {

   public xy( String applicationTitle, String chartTitle,int [][]mat, int alto, int ancho ,int inicodevectestado, int finaldevectesado ) {
      super(applicationTitle);
      
      int res[][]= new int[alto][ancho]; 
        for(int x=0; x<alto; x++){
            for(int i=0; i<ancho; i++){
                res[x][i]=mat[x][i];
            }
        }
        int anch=ancho;
        int alt=alto;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
      JFreeChart xylineChart = ChartFactory.createXYLineChart(
         chartTitle ,
         "" ,
         "" ,
         createDataset(res,alt,anch,vectestadoin,vectestadofin) ,
         PlotOrientation.VERTICAL ,
         true , true , false);
         
      ChartPanel chartPanel = new ChartPanel( xylineChart );
      chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
      final XYPlot plot = xylineChart.getXYPlot( );
      
      XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
      renderer.setSeriesPaint( 0 , Color.PINK );
      renderer.setSeriesPaint( 1 , Color.BLUE);
      renderer.setSeriesStroke( 0 , new BasicStroke( 4.0f ) );
      renderer.setSeriesStroke( 1 , new BasicStroke( 3.0f ) );
      plot.setRenderer( renderer ); 
      setContentPane( chartPanel ); 
   }
   
   private XYDataset createDataset(int [][]mat, int alto, int ancho,int inicodevectestado, int finaldevectesado) {
      int res[][]= new int[alto][ancho];
        for(int x=0; x<alto; x++){
            for(int i=0; i<ancho; i++){
                res[x][i]=mat[x][i];
            }
        }
        int anch=ancho;
        int alt=alto;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        //aqui sera como los items de el combobox donde solopondremos y se hara como los otros donde empieza y contador
        //más info en barras
        // solo que aqui el estado sera nuestra x en la grafíca 
        // dado que no encontre alguna forma de mostrarlo más claramente
         int vectestado[]= new int [6];
        vectestado[0]=1;
        vectestado[1]=19;
        vectestado[2]=24;
        vectestado[3]=20;
        vectestado[4]=10;
        vectestado[5]=32;
        XYSeries hombres= new XYSeries("Hombres");
        XYSeries mujeres= new XYSeries("Mujeres");
        for(int x2=0; x2<alt; x2++){
            int a=vectestadoin; // esta es la que tendra la pocicion donde inician los estados
            //el ancho sera la canidad numerica de diferencia entre la posicion inicial y la final de los esatdos 
            //esto se repitira en todas las claces incluso en las one creo que lo de ancho diferente de uno debe ser cambiado dado que puede ser que
            // quieran solo de un estado talves si ese sea el caso mandemos un numero fuera del paramentto de los combo box como valor inicial y el limite 
            // que sea el estado así se podria realizar
            // o que sea una nueva condicion el limite
            for(int i2=0; i2<anch; i2++){
                if(x2==0 && ancho!=1  ){
                mujeres.add(vectestado[a], new Double(res[x2][i2]) );
               }
                else if(x2==1 && ancho!=1){
                hombres.add(vectestado[a], new Double(res[x2][i2]));
                }
                else if(x2==0 && ancho==1 && vectestadofin==-1 ){
                   mujeres.add(vectestado[vectestadoin], new Double(res[x2][i2]) ); 
                }
                else if(x2==1 && ancho==1 && vectestadofin==-1){
                   hombres.add(vectestado[vectestadoin], new Double(res[x2][i2]) ); 
                }
                else if(x2==0 && ancho==1 && vectestadofin==0){
                   mujeres.add(0, new Double(res[x2][i2])); 
                }
               else if(x2==1 && ancho==1 && vectestadofin==0){
                   hombres.add(0, new Double(res[x2][i2]) ); 
                } 
                a=a+1;// lo que ara moverse dentro del vector de estados
            }
        }
      XYSeriesCollection dataset = new XYSeriesCollection( );          
      dataset.addSeries(mujeres);          
      dataset.addSeries(hombres);    
      return dataset;
   }
}

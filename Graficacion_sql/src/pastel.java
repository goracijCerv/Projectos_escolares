/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JPanel;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.general.DefaultPieDataset;
import org.jfree.data.general.PieDataset;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;


/**
 *
 * @author horacio
 */
public class pastel extends ApplicationFrame{
    
    public pastel(String title, int [][]mat, int alto, int ancho, int limedad, int limeadad2,int inicodevectestado, int finaldevectesado) {
        super(title);
        int res[][]= new int[alto][ancho];
        int as=limedad;
        int as2= limeadad2;
        for(int x=0; x<alto; x++){
            for(int i=0; i<ancho; i++){
                res[x][i]=mat[x][i];
            }
        }
        int anch=ancho;
        int alt=alto;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        setContentPane(createDemoPanel(res,alt,anch,as,as2,vectestadoin,vectestadofin));
        
    }
    private static PieDataset createDataset(int [][]mat, int alto, int ancho, int limedad, int limeadad2,int inicodevectestado, int finaldevectesado){
        int res[][]= new int[alto][ancho];
        int as=limedad;
        int as2= limeadad2;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        String vectestado[]= new String[6];
        vectestado[0]="AGS";
        vectestado[1]="MTY";
        vectestado[2]="SLP";
        vectestado[3]="OAX";
        vectestado[4]="DUR";
        vectestado[5]="ZAC";
        
        for(int x=0; x<alto; x++){
            for(int i=0; i<ancho; i++){
                res[x][i]=mat[x][i];
            }
        }
       
        DefaultPieDataset dataset = new DefaultPieDataset( );
        for(int x2=0; x2<alto; x2++){
            int  inicio=vectestadoin;
            for(int i2=0; i2<ancho; i2++){
                if(x2==0 && ancho!=1 && as!=0 && vectestadofin!=-1 ){
                dataset.setValue( "Mujeres entre los "+as+" y los "+as2+"años del esatdo "+ vectestado[inicio] , new Double( res[x2][i2] ) );
               }
               else if(x2==0 && ancho==1 && as!=0 && vectestadofin ==-1 ){
                dataset.setValue( "Mujeres entre los "+as+" y los "+as2+"años del esatdo "+ vectestado[vectestadoin] , new Double( res[x2][i2] ) );
               }
                
               else if(x2==0 && ancho==1 && as!=0 && vectestadofin ==0 ){
                dataset.setValue( "Mujeres entre los "+as+" y los "+as2, new Double( res[x2][i2] ) );
               }
               
               else if(x2==1 && ancho!=1 && as!=0 && vectestadofin!=-1){
               dataset.setValue( "Hombres entre los "+as+" y los "+as2+"años del esatdo "+ vectestado[inicio] , new Double( res[x2][i2] ) );
               }
               
               else if(x2==1 && ancho==1 && as!=0 && vectestadofin==-1){
               dataset.setValue( "Hombres entre los "+as+" y los "+as2+"años del esatdo "+ vectestado[vectestadoin] , new Double( res[x2][i2] ) );
               }
               
               else if(x2==1 && ancho==1 && as!=0 && vectestadofin==0){
               dataset.setValue( "Hombres entre los "+as+" y los "+as2 , new Double( res[x2][i2] ) );
               }
               
               else if(x2==0 && ancho!=1 && as==0 && vectestadofin!=-1 ){
                dataset.setValue( "Mujeres  del esatdo "+ vectestado[inicio] , new Double( res[x2][i2] ) );
               }
               else if(x2==0 && ancho==1 && as==0 && vectestadofin ==-1 ){
                dataset.setValue( "Mujeres entre del esatdo "+ vectestado[vectestadoin] , new Double( res[x2][i2] ) );
               }
                
               else if(x2==0 && ancho==1 && as==0 && vectestadofin ==0 ){
               dataset.setValue( "Mujeres ", new Double( res[x2][i2] ) );
               }
               
               else if(x2==1 && ancho!=1 && as==0 && vectestadofin!=-1){
               dataset.setValue( "Hombres entre los  del esatdo "+ vectestado[inicio] , new Double( res[x2][i2] ) );
               }
               
               else if(x2==1 && ancho==1 && as==0 && vectestadofin==-1){
               dataset.setValue( "Hombres entre los  del esatdo "+ vectestado[vectestadoin] , new Double( res[x2][i2] ) );
               }
               
               else if(x2==1 && ancho==1 && as==0 && vectestadofin==0){
               dataset.setValue( "Hombres " , new Double( res[x2][i2] ) );
               }
                
                
                inicio=inicio+1;
            }
        }
        return dataset;
    }
    
    private static JFreeChart createChart( PieDataset dataset ) {
      JFreeChart chart = ChartFactory.createPieChart(      
         "",   // chart title 
         dataset,          // data    
         true,             // include legend   
         true, 
         false);

      return chart;
   }
   
   public static JPanel createDemoPanel(int [][]mat, int alto, int ancho, int limedad, int limeadad2, int inicodevectestado, int finaldevectesado ) {
       int res[][]= new int[alto][ancho];
        int as=limedad;
        int as2= limeadad2;
        for(int x=0; x<alto; x++){
            for(int i=0; i<ancho; i++){
                res[x][i]=mat[x][i];
            }
        }
        int anch=ancho;
        int alt=alto;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
      JFreeChart chart = createChart(createDataset(res,alt,anch,as,as2,vectestadoin,vectestadofin) );  
      return new ChartPanel( chart ); 
   }
}

//crear paramentro de rango de estados donde ae nos indicara de donde inicia hasta donde termina 
// y despues solo hacemos un contador para poder saber cunto sera nuestro valor de anchura
//para cambiar solo hacemos un contador desde donde inicie 
//tambien se ralizaria para pastelone y los demas graficos
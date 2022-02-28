/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author horacio
 */
import org.jfree.chart.ChartPanel;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

public class lineas extends ApplicationFrame {

   public lineas( String applicationTitle , String chartTitle, int [][]mat, int alto, int ancho, int limedad, int limeadad2,int inicodevectestado, int finaldevectesado ) {
      super(applicationTitle);
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
      JFreeChart lineChart = ChartFactory.createLineChart(
         chartTitle,
         "","",
         createDataset(res,alto,ancho,as,as2,vectestadoin,vectestadofin),
         PlotOrientation.VERTICAL,
         true,true,false);
         
      ChartPanel chartPanel = new ChartPanel( lineChart );
      chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
      setContentPane( chartPanel );
   }

   private DefaultCategoryDataset createDataset(int [][]mat, int alto, int ancho, int limedad, int limeadad2 ,int inicodevectestado, int finaldevectesado ) {
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
         String vectestado[]= new String[6];
         vectestado[0]="AGS";
        vectestado[1]="MTY";
        vectestado[2]="SLP";
        vectestado[3]="OAX";
        vectestado[4]="DUR";
        vectestado[5]="ZAC";

       DefaultCategoryDataset dataset = new DefaultCategoryDataset( );
       for(int x2=0; x2<alt; x2++){
           int inicio=vectestadoin;
            for(int i2=0; i2<anch; i2++){
                if(x2==0 && ancho!=1 && as!=0 ){
                dataset.setValue( new Double( res[x2][i2]), "Mujeres entre los "+as+" y los "+as2+" años", vectestado[inicio]);
               }
                else if(x2==1 && ancho!=1 && as!=0){
                dataset.setValue( new Double( res[x2][i2]), "Hombres entre los "+as+" y los "+as2+" años", vectestado[inicio] );
                }
                else if(x2==0 && ancho==1 && as!=0 && vectestadofin ==-1){
                   dataset.setValue( new Double( res[x2][i2]), "Mujeres entre los "+as+" y los "+as2+"años",vectestado[vectestadoin]); 
                }
                else if(x2==1 && ancho==1 && as!=0 && vectestadofin==-1 ){
                   dataset.setValue( new Double( res[x2][i2]), "Hombres entre los "+as+" y los "+as2+"años",vectestado[vectestadoin] ); 
                }
                
                else if(x2==0 && ancho==1 && as!=0 && vectestadofin ==0){
                   dataset.setValue( new Double( res[x2][i2]), "Mujeres entre los "+as+" y los "+as2+"años","Totales"); 
                }
                else if(x2==1 && ancho==1 && as!=0 && vectestadofin==0 ){
                   dataset.setValue( new Double( res[x2][i2]), "Hombres entre los "+as+" y los "+as2+"años","Totales" ); 
                }
                
               else if(x2==0 && ancho!=1 && as==0 ){
                dataset.setValue( new Double( res[x2][i2]), "Mujeres", vectestado[inicio]);
               }
                else if(x2==1 && ancho!=1 && as==0){
                dataset.setValue( new Double( res[x2][i2]), "Hombres", vectestado[inicio] );
                }
                else if(x2==0 && ancho==1 && as==0 && vectestadofin ==-1){
                   dataset.setValue( new Double( res[x2][i2]), "Mujeres ",vectestado[vectestadoin]); 
                }
                else if(x2==1 && ancho==1 && as==0 && vectestadofin==-1 ){
                   dataset.setValue( new Double( res[x2][i2]), "Hombres ",vectestado[vectestadoin] ); 
                }
                
                else if(x2==0 && ancho==1 && as==0 && vectestadofin ==0){
                   dataset.setValue( new Double( res[x2][i2]), "Mujeres","Totales"); 
                }
                else if(x2==1 && ancho==1 && as==0 && vectestadofin==0 ){
                   dataset.setValue( new Double( res[x2][i2]), "Hombres", "Totales" ); 
                }
                
                inicio=inicio+1;
            }
        }
      return dataset;
   }
}

//recuerda que falta todo lo que va en el main de barras,barrasone,lineas,lineasone,xy,xyone, 
//asi que espero que para el lunes cunado sepamos los rangos de los esados se pueda hacer

import java.awt.BasicStroke;
import java.awt.Color;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
import org.jfree.ui.ApplicationFrame;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author horacio
 */
public class xyone extends ApplicationFrame {
    public xyone(String applicationTitle , String chartTitle, int []mat, int ancho, int sex, int inicodevectestado, int finaldevectesado){
        super( applicationTitle );
      int res[]= new int[ancho];
        System.arraycopy(mat, 0, res, 0, ancho);
        int anch=ancho;
        int rio=sex;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        JFreeChart xylineChart = ChartFactory.createXYLineChart(
         chartTitle ,
         "" ,
         "" ,
        createDataset(res,ancho,rio,vectestadoin,vectestadofin),
        PlotOrientation.VERTICAL ,
         true , true , false);
         
      ChartPanel chartPanel = new ChartPanel( xylineChart );
      chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
      final XYPlot plot = xylineChart.getXYPlot( );
      
      XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
      renderer.setSeriesPaint( 0 , Color.GRAY );
      renderer.setSeriesStroke( 0 , new BasicStroke( 4.0f ) );
      plot.setRenderer( renderer ); 
      setContentPane( chartPanel ); 
    }
    private XYDataset createDataset(int []mat, int ancho, int sex,int inicodevectestado, int finaldevectesado) {
      int res[]= new int[ancho];
        System.arraycopy(mat, 0, res, 0, ancho);
        int anch=ancho;
        int rio=sex;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        int vectestado[]= new int [6];
        vectestado[0]=1;
        vectestado[1]=0;
        vectestado[2]=0;
        vectestado[3]=0;
        vectestado[4]=0;
        vectestado[5]=0;
        
        if(rio==0){
            XYSeries neutral= new XYSeries("Mujeres");
            int a=vectestadoin;
        for(int i2=0; i2<ancho; i2++){
                if(ancho!=1 ){
                neutral.add(vectestado[a], new Double(res[i2]) );
               }
                
                else if(ancho==1 && vectestadofin==-1){
                   neutral.add(vectestado[vectestadoin], new Double(res[i2]) ); 
                }
                else if(ancho==1 && vectestadofin==0){
                   neutral.add(0, new Double(res[i2])); 
                }
               
                a=a+1;// lo que ara moverse dentro del vector de estados
            }
           XYSeriesCollection dataset = new XYSeriesCollection( );
           dataset.addSeries(neutral);
           return dataset;
        }
        else if(rio==1){
            XYSeries neutral= new XYSeries("Hombres");
            int a=vectestadoin;
        for(int i2=0; i2<ancho; i2++){
                if(ancho!=1 ){
                neutral.add(vectestado[a], new Double(res[i2]) );
               }
                
                else if(ancho==1 && vectestadofin==-1){
                   neutral.add(vectestado[vectestadoin], new Double(res[i2]) ); 
                }
                else if(ancho==1 && vectestadofin==0){
                   neutral.add(0, new Double(res[i2])); 
                }
               
                a=a+1;// lo que ara moverse dentro del vector de estados
            }
          XYSeriesCollection dataset = new XYSeriesCollection( );
           dataset.addSeries(neutral);
           return dataset;
        
        }
        else{
            XYSeries neutral= new XYSeries("Personas");
            int a=vectestadoin;
        for(int i2=0; i2<ancho; i2++){
                if(ancho!=1 ){
                neutral.add(vectestado[a], new Double(res[i2]) );
               }
                
                else if(ancho==1 && vectestadofin==-1){
                   neutral.add(vectestado[vectestadoin], new Double(res[i2]) ); 
                }
                else if(ancho==1 && vectestadofin==0){
                   neutral.add(0, new Double(res[i2])); 
                }
               
                a=a+1;// lo que ara moverse dentro del vector de estados
            }
        XYSeriesCollection dataset = new XYSeriesCollection( );
           dataset.addSeries(neutral);
           return dataset;
        
        }
   }
    
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import org.jfree.chart.ChartPanel;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;
/**
 *
 * @author horacio
 */
public class lineasone extends ApplicationFrame {
    
    public lineasone(String applicationTitle , String chartTitle, int []mat, int ancho, int limedad, int limeadad2,  int sex ,int inicodevectestado, int finaldevectesado){
        super( applicationTitle );
      int res[]= new int[ancho];
        System.arraycopy(mat, 0, res, 0, ancho);
        int as=limedad;
        int as2= limeadad2;
        int anch=ancho;
        int rio=sex;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        JFreeChart lineChart = ChartFactory.createLineChart(
         chartTitle,
         "","",
         createDataset(res,ancho,as,as2,rio,vectestadoin,vectestadofin),
         PlotOrientation.VERTICAL,
         true,true,false);
       ChartPanel chartPanel = new ChartPanel( lineChart );
      chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
      setContentPane( chartPanel );
    }
    
    private DefaultCategoryDataset createDataset(int []mat, int ancho, int limedad, int limeadad2,  int sex ,int inicodevectestado, int finaldevectesado ){
        int res[]= new int[ancho];
        System.arraycopy(mat, 0, res, 0, ancho);
        int as=limedad;
        int as2= limeadad2;
        int anch=ancho;
        int rio=sex;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
         String vectestado2[]= new String[6];
        vectestado2[0]="AGS";
        vectestado2[1]="MTY";
        vectestado2[2]="SLP";
        vectestado2[3]="OAX";
        vectestado2[4]="DUR";
        vectestado2[5]="ZAC";
        
        DefaultCategoryDataset dataset = new DefaultCategoryDataset( );
        int inicio=vectestadoin;
        for(int asa=0; asa<ancho; asa++){
            if(rio==0 && anch!=1 && as!=0){
            dataset.setValue(new Double( res[asa]),"Mujeres entre los "+as+" y los "+as2+"años", vectestado2[inicio]);
            }
            else if(rio==1 && anch!=1 &&as!=0){
            dataset.setValue( new Double( res[asa]),"Hombres entre los "+as+" y los "+as2+"años", vectestado2[inicio] ); 
            }
            else if(rio==0 && anch==1 && as!=0 && vectestadofin==-1){
            dataset.setValue(new Double( res[asa] ), "Mujeres entre los "+as+" y los "+as2+"años", vectestado2[vectestadoin]);
            }
            else if(rio==1 && anch==1 && as!=0 && vectestadofin==-1){
            dataset.setValue( new Double( res[asa] ), "Hombres entre los "+as+" y los "+as2+"años", vectestado2[vectestadoin] );
            }
            else if(rio==0 && anch==1 && as!=0 && vectestadofin==0){
            dataset.setValue(new Double( res[asa] ), "Mujeres ","entre los "+as+" y los "+as2+"años");
            }
            else if(rio==1 && anch==1 && as!=0 && vectestadofin==0){
            dataset.setValue( new Double( res[asa] ), "Hombres", "entre los "+as+" y los "+as2+"años" );
            }
            
            else if(rio==0 && anch!=1 && as==0){
            dataset.setValue(new Double( res[asa]),"Mujeres ", vectestado2[inicio]);
            }
            else if(rio==1 && anch!=1 && as==0){
            dataset.setValue( new Double( res[asa]),"Hombres ", vectestado2[inicio] ); 
            }
            else if(rio==0 && anch==1 && as==0 && vectestadofin==-1){
            dataset.setValue(new Double( res[asa] ), "Mujeres ", vectestado2[vectestadoin]);
            }
            else if(rio==1 && anch==1 && as==0 && vectestadofin==-1){
            dataset.setValue( new Double( res[asa] ), "Hombres ", vectestado2[vectestadoin] );
            }
            else if(rio==0 && anch==1 && as==0 && vectestadofin==0){
            dataset.setValue(new Double( res[asa] ), "Mujeres ","Totales");
            }
            else if(rio==1 && anch==1 && as==0 && vectestadofin==0){
            dataset.setValue( new Double( res[asa] ), "Hombres", "Totales" );
            }
            
            else if(rio==2 && anch!=1 && as!=0){
             dataset.setValue( new Double( res[asa]),"Personas entre los "+as+" y los "+as2+"años", vectestado2[inicio] ); 
            }
            else if(rio==2 && anch==1 && as!=0 && vectestadofin==-1){
             dataset.setValue( new Double( res[asa] ), "Personas entre los "+as+" y los "+as2+"años",vectestado2[vectestadoin]); 
            }
            
            else if(rio==2 && anch==1 && as!=0 && vectestadofin==0){
             dataset.setValue( new Double( res[asa] ), "Personas", "entre los "+as+" y los "+as2+"años"); 
            }
            
            else if(rio==2 && anch!=1 && as==0){
             dataset.setValue( new Double( res[asa]),"Personas", vectestado2[inicio] ); 
            }
            else if(rio==2 && anch==1 && as==0 && vectestadofin==-1){
             dataset.setValue( new Double( res[asa] ), "Personas",vectestado2[vectestadoin]); 
            }
            
            else if(rio==2 && anch==1 && as==0 && vectestadofin==0){
             dataset.setValue( new Double( res[asa] ), "Personas", "Totales"); 
            }
            
          inicio=inicio+1;   
       }
        return dataset;
    }
    
}

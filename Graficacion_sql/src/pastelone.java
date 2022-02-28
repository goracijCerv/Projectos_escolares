/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author horacio
 */
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
public class pastelone extends ApplicationFrame{
    
    public pastelone(String title, int []mat, int ancho, int limedad, int limeadad2,  int sex,int inicodevectestado, int finaldevectesado ) {
        super(title);
        int res[]= new int[mat.length];
        System.arraycopy(mat, 0, res, 0, mat.length);
        int as=limedad;
        int as2= limeadad2;
        int anch=ancho;
        int rio=sex;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
        setContentPane(createDemoPanel(res,anch,as,as2,rio,vectestadoin,vectestadofin));
        
    }
    private static PieDataset createDataset(int []mat, int ancho, int limedad, int limeadad2, int sex ,int inicodevectestado, int finaldevectesado){
        int res[]= new int[mat.length];
        System.arraycopy(mat, 0, res, 0, mat.length);
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
        DefaultPieDataset dataset = new DefaultPieDataset( );
        int inicio=vectestadoin;
       for(int asa=0; asa<ancho; asa++){
          
            if(rio==0 && anch!=1 && as!=0){
            dataset.setValue( "Mujeres entre los "+as+" y los "+as2+"años del esatdo "+ vectestado2[inicio] , new Double( res[asa] ) );
            }
            else if(rio==1 && anch!=1 &&as!=0){
            dataset.setValue( "Hombres entre los "+as+" y los "+as2+"años del esatdo "+ vectestado2[inicio] , new Double( res[asa] ) ); 
            }
            else if(rio==0 && anch==1 && as!=0 && vectestadofin==-1){
            dataset.setValue( "Mujeres entre los "+as+" y los "+as2+"años del estado "+ vectestado2[vectestadoin] , new Double( res[asa] ) );
            }
            
             else if(rio==0 && anch==1 && as!=0 && vectestadofin==0){
            dataset.setValue( "Mujeres entre los "+as+" y los "+as2 , new Double( res[asa] ) );
            }
            
            else if(rio==1 && anch==1 && as!=0 && vectestadofin==-1){
            dataset.setValue( "Hombres entre los "+as+" y los "+as2+"años del estado "+ vectestado2[vectestadoin] , new Double( res[asa] ) );
            }
            
             else if(rio==1 && anch==1 && as!=0 && vectestadofin==0){
            dataset.setValue( "Hombres entre los "+as+" y los "+as2+"años" , new Double( res[asa] ) );
            }
            
            else if(rio==0 && anch!=1 && as==0){
            dataset.setValue( "Mujeres entre los del esatdo "+ vectestado2[inicio] , new Double( res[asa] ) );
            }
            else if(rio==1 && anch!=1 && as==0){
            dataset.setValue( "Hombres entre los del esatdo "+ vectestado2[inicio] , new Double( res[asa] ) ); 
            }
            else if(rio==0 && anch==1 && as==0 && vectestadofin==-1){
            dataset.setValue( "Mujeres entre los del estado "+ vectestado2[vectestadoin] , new Double( res[asa] ) );
            }
            
             else if(rio==0 && anch==1 && as==0 && vectestadofin==0){
            dataset.setValue( "Mujeres" , new Double( res[asa] ) );
            }
            
            else if(rio==1 && anch==1 && as==0 && vectestadofin==-1){
            dataset.setValue( "Hombres entre del estado "+ vectestado2[vectestadoin] , new Double( res[asa] ) );
            }
            
            else if(rio==1 && anch==1 && as==0 && vectestadofin==0){
            dataset.setValue( "Hombres " , new Double( res[asa] ) );
            }
            
            else if(rio==2 && anch!=1 &&as!=0){
            dataset.setValue( "Personas entre los "+as+" y los "+as2+"años del esatdo "+ vectestado2[inicio] , new Double( res[asa] ) ); 
            }
            
            else if(rio==2 && anch==1 && as!=0 && vectestadofin==-1){
            dataset.setValue( "Personas entre los "+as+" y los "+as2+"años del estado "+ vectestado2[vectestadoin] , new Double( res[asa] ) );
            }
            
            else if(rio==2 && anch==1 && as!=0 && vectestadofin==0){
            dataset.setValue( "Personas entre los "+as+" y los "+as2+"años" , new Double( res[asa] ) );
            }
            
            else if(rio==2 && anch!=1 && as==0){
            dataset.setValue( "Personas entre los del esatdo "+ vectestado2[inicio] , new Double( res[asa] ) ); 
            }
            
            else if(rio==2 && anch==1 && as==0 && vectestadofin==-1){
            dataset.setValue( "Personas entre del estado "+ vectestado2[vectestadoin] , new Double( res[asa] ) );
            }
            
            else if(rio==2 && anch==1 && as==0 && vectestadofin==0){
            dataset.setValue( "Personas " , new Double( res[asa] ) );
            }
            inicio=inicio+1;
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
   
   public static JPanel createDemoPanel(int []mat, int ancho, int limedad, int limeadad2, int sex,int inicodevectestado, int finaldevectesado ) {
       int res[]= new int[mat.length];
        System.arraycopy(mat, 0, res, 0, mat.length);
        int as=limedad;
        int as2= limeadad2;
        int anch=ancho;
        int rio=sex;
        int vectestadoin=inicodevectestado;
        int vectestadofin=finaldevectesado;
      JFreeChart chart = createChart(createDataset(res,anch,as,as2,rio,vectestadoin,vectestadofin) );  
      return new ChartPanel( chart ); 
   }
}


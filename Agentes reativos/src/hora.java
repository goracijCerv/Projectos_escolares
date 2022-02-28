

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author horacio
 */
public class hora extends Thread {
    private String fec=null;
    public hora(){
        
    }
    @Override
    public void run(){
        
        while(true){
            Date fecha= new Date();
            DateFormat fecha2= new SimpleDateFormat("HH:mm:ss 'del dia' dd/MM/yyyy");
            this.fec=fecha2.format(fecha);
            System.out.println(fec);
           
            try {
                Thread.sleep(1000);
                 
            } catch (InterruptedException ex) {
                Logger.getLogger(hora.class.getName()).log(Level.SEVERE, null, ex);
            }
        }   
    }
     public String a(){
            return this.fec;
        }
}

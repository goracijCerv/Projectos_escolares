
import java.io.File;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
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
public class archivo extends Thread {
    private File seguir=null;
    private String fec=null;
    private int conf=0;
    public archivo(){
        
    }
    @Override
    public void run(){
        boolean c =true;
        while(c==true){
            StringBuilder a= new StringBuilder();
        long ms =seguir.lastModified();
        Date d = new Date(ms);
        Calendar cr= new GregorianCalendar();
        cr.setTime(d);
        String[] a2= new String[6];
        a2[0]=Integer.toString(cr.get(Calendar.SECOND));
        a2[1]=Integer.toString(cr.get(Calendar.MINUTE));
        a2[2]=Integer.toString(cr.get(Calendar.HOUR));
        a2[3]=Integer.toString(cr.get(Calendar.DATE));
        a2[4]=Integer.toString(cr.get(Calendar.MONTH));
        a2[5]=Integer.toString(cr.get(Calendar.YEAR));
        for(int i=0; i<6; i++){
            a.append(a2[i]);
            a.append("/");
        }
        String aw =a.toString();
        if( !aw.equals(fec)){
           c=false;
           System.out.println("a ocurido un cambio");
            JOptionPane.showMessageDialog(null,"El archivo hacido modificado");
           this.conf=1;
           
        }
        }
        
    }
    public String fecha(File xd){
        StringBuilder a= new StringBuilder();
        long ms =seguir.lastModified();
        Date d = new Date(ms);
        Calendar c= new GregorianCalendar();
        c.setTime(d);
        String[] a2= new String[6];
        a2[0]=Integer.toString(c.get(Calendar.SECOND));
        a2[1]=Integer.toString(c.get(Calendar.MINUTE));
        a2[2]=Integer.toString(c.get(Calendar.HOUR));
        a2[3]=Integer.toString(c.get(Calendar.DATE));
        a2[4]=Integer.toString(c.get(Calendar.MONTH));
        a2[5]=Integer.toString(c.get(Calendar.YEAR));
        for(int i=0; i<6; i++){
            a.append(a2[i]);
            a.append("/");
        }
        String aw =a.toString();
        return aw;
    }
    public void valor(File s){
        this.seguir=s;
        this.fec=fecha(s);
    }
    public int confirmar(){
        return this.conf;
    }
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package back;
import java.util.Scanner;
/**
 *
 * @author horacio
 */
public class MMP {

    /**;
     * @param args the command line arguments
     */
    public static void minmon(int mon[],int tot, int cant){
        int p,mone,min,i;
        //creando los vectores temporales
        int[]Cminmon=new int[tot+1];
        int[]Smon=new int[tot+1];
        //iniciamos con cero en dado caso que incerten cero.
        Cminmon[0]=0;
        Smon[0]=0;
        mone=0;
        //iniciamos P hasta que sea el total.
        for(p=1;p<=tot;p++){
        //poniendo un valor muy grnade para la cantidad minima de monedas dado
        //que no sabemos cuantas se necesiten, el proceso se repitira
        //hasta que p llegue a la cantidad total.
        min=10000;
        //iniciamos un ciclo para que recora las monedas disponibles.
        // y encuentre la cantidad minima de monedas para la canridad P
        // es decir el vector contendra la cantidad minima para 1 hasta la cantidad n del cambio
          for(i=0; i<cant;i++){
              if(mon[i]<=p){
                  if(1 + Cminmon[p-mon[i]]<min){
                      min= 1 + Cminmon[p-mon[i]];
                      mone=i;
                  }
              }
          }
          Cminmon[p]=min;
          Smon[p]=mone;
        }
        impmonus(mon,Smon,tot);
    }
    public static void impmonus(int mon[], int Smon[],int tot){
        int a=tot;
        while(a>0){
            System.out.println("Moneda usada: " + mon[Smon[a]]);
            a=a-mon[Smon[a]];
        }
    }
    public static void main(String[] args) {
        // TODO code application logic here
        int[] monedas={1,2,5,12};
        for(int i=0;i<monedas.length; i++){
            System.out.println("Las monedas disponbles son: "+ monedas[i]);
        }
        Scanner ob= new Scanner(System.in);
        System.out.println("Incerte la cantidad deseada de cambio ");
        int total=ob.nextInt();
        minmon(monedas,total,monedas.length);
    }
    
}

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
 * problema de la moneda con un enfoque de divide y venceras
 * nota: como se sabe no todas las tecnincas son efectivas
 * en ciertos problemas y en el caso del problema de la moneda
 * se da esta situacion, si llegua a una respuesta pero
 * tarda demaciado, es por eso que la version con programacion 
 * dinamica es mucho mejor, corrigueindo este error. 
 */
public class DyVMP {

    /**
     * @param args the command line arguments
     */
    public static int minmonedas(int V,int monedas[]){
        int[] csol,misol;
        csol=new int[monedas.length];
        misol=new int[monedas.length];
        int solfin;
        //el caso base seria que nos pidieran cambio para cero
        if(V==0){
            return 0;
        }
        
        for(int i=0; i<monedas.length; i++){
            //despues los siguientes casos seria que nuestra moneda i fuera menor al valor establecido
            if(V>=monedas[i]){
                //al comprobar esto volvemos a llmar la funcion para resolver un problema mas simple dado que 
                //estamos buscando la cantidad minima para un problema menor
                        csol[i]=minmonedas(V-monedas[i],monedas);
                        misol[i]=csol[i]+1;
            }
        }
        //una vez pasados por todas las cantidades de monedas necesarias para la cantidad pedida de las monedas disponiles
        //buscamos el minimo de estas, las cuales se almecenaron en misol
        //buscando el minimo 
        solfin=1000000000;
        for(int j=0; j<monedas.length; j++){
            if(misol[j]>0){
                if(misol[j]<solfin){
                    solfin=misol[j];
                }
            }
        }
        return solfin;
    }
    public static void main(String[] args) {
        // TODO code application logic here
         int[] monedas={1,2,5,12};
         int respuesta;
        for(int i=0;i<monedas.length; i++){
            System.out.println("Las monedas disponbles son: "+ monedas[i]);
        }
        Scanner ob= new Scanner(System.in);
        System.out.println("Incerte la cantidad deseada de cambio ");
        int total=ob.nextInt();
        respuesta=minmonedas(total,monedas);
        System.out.println("la cantidad minima de monedas para formar "+ total+ " es de "+ respuesta +" monedas");
    }
    
}

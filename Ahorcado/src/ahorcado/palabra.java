/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ahorcado;

/**
 *
 * @author horacio
 */
public class palabra {
  protected String[] palabras= new String[5];
   protected  int rand;
 public void setpalabras(int n){
     switch(n){
         case 1:{
             this.palabras[0]="casa";
             this.palabras[1]="tamal";
             this.palabras[2]="pato";
             this.palabras[3]="dedo";
             this.palabras[4]="alma";
             break;
         }
         case 2:{
             this.palabras[0]="casa";
             this.palabras[1]="posol";
             this.palabras[2]="taco";
             this.palabras[3]="bastardo";
             this.palabras[4]="ceniza";
             break;
         }
         case 3:{
             this.palabras[0]="exterminio";
             this.palabras[1]="vendrick";
             this.palabras[2]="astorias";
             this.palabras[3]="taquisa";
             this.palabras[4]="colibri";
             break;
         }
         
     }
 }   
 public void restet(){
     for(int h=0; h<5; h++){
       this.palabras[h]=null;
     }
 }
}

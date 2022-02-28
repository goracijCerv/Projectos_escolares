/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package back;
import java.util.Comparator;
import java.util.Arrays;
/**
 *
 * @author horacio
 * http://www.mathcs.emory.edu/~cheung/Courses/253/Syllabus/DynProg/money-change.html divide y venceras 
 * http://www.cs.uni.edu/~fienup/cs188s05/lectures/lec6_1-27-05.htm
 */
public class Main {
public static double mochilagreedy(int[] peso,int[] valor,int capasidad){
    //creamos un vector de objetos de item lo cual nos representa el objeto en si
    item[] items=new item[peso.length];
    //pasamos cada valor y peso a su reprentativo objeto item y optenemos su coste
    for(int i=0;i<peso.length;i++){
       items[i]=new item(valor[i],peso[i],i); 
    }
    // se ordena el vector gracias al metodo de array short,
    //basandonos a la compracion del coste, el cual es clasificado por 
    //un compere el cual retrorna un valor cero si el coste es igual, un valor 
    // negativo si este es menor y un valor positivo si este es mayor
   Arrays.sort(items, new Comparator<item>() {
            @Override
            public int compare(item ob1, item ob2)
            {
                return ob2.coste.compareTo(ob1.coste);
            }
        });
   /*for(int i=0;i<peso.length;i++){
       System.out.println(items[i].coste);
    }*/
   double valortot=0;
   double cap=capasidad;
   int j=0;
   while(cap!=0){
       if(items[j].peso<=cap){
           //significa que puede tomar el objeto completo
           valortot=valortot+items[j].valor;
           cap=cap-items[j].peso;
       }else{
           //significa que tiene que tomar un pedaso de este
           double fracion=cap/items[j].peso;
           valortot=valortot+(fracion*items[j].valor);
           cap=0;
       }
       j++;
   }
   return valortot;
}

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int[] pesos = { 10, 40, 20, 30 };
        int[] valores = { 60, 40, 100, 120 };
        int capacidad = 50;
 
        double valormax = mochilagreedy(pesos, valores, capacidad);
        System.out.println("El valor maximo optenido fue " + valormax);
    }
    
}

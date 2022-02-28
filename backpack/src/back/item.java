/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package back;

/**
 *
 * @author horacio
 */
public class item {
    Double coste; //se necetia usar un objeto para usar compare
    double valor,peso,id;
    public item(int valor,int peso, int id){
        this.valor=valor;
        this.peso=peso;
        this.id=id;
        coste=new Double((double)valor / (double)peso);
    }
}
//informacion relevante accerca del funcionamiento de compere y 
//https://www.youtube.com/watch?v=-gDKPs2Bl60
//https://aprenderaprogramar.com/foros/index.php?topic=4794.0#:~:text=En%20Java%20no%20es%20lo,de%20dato%20denominado%20%22objeto%22.&text=En%20este%20ejercicio%20se%20pide%20usar%20double%20(el%20tipo%20primitivo).

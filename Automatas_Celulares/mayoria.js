//Implementacion de la regla de la mayoria pero se evaluan los vecinos de a lado
function tablero(col, fil) { //creando el tablero del juego
    let y = new Array(col);
    for (let i = 0; i < y.length; i++) {
        y[i] = new Array(fil);
    }
    return y
}
let columnas;
let filas;
let resolucion = 10; //ayuda a darle un tamaño a las celulas  
let tablero2;

function setup() { //inicando el juego
    createCanvas(1320, 620);
    columnas = width / resolucion;
    filas = height / resolucion;
    tablero2 = tablero(columnas, filas);
    for (let i = 0; i < columnas; i++) {
        for (let j = 0; j < 1; j++) {
            tablero2[i][j] = floor(random(2)); //iniciamos con celulas vivias y muertas de forma aleatoria
        }
    }

}

function draw() { //establecemos el tablero
    background(0);
    for (let i = 0; i < columnas; i++) {
        for (let j = 0; j < filas; j++) {
            let x = i * resolucion;
            let y = j * resolucion;
            if (tablero2[i][j] == 1) {
                fill(125, 33, 129); //color de los vivos
                stroke(125, 33, 129);
                rect(x, y, resolucion - 1, resolucion - 1);
            }

        }
    }
    //calcular los siguientes estado
    for (let i = 0; i < columnas; i++) {
        for (let j = 1; j < filas; j++) {
            if (tablero2[i][j - 1] == 0 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 1 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 1) {
                tablero2[i][j] = 1; //vivo  
            } else if (tablero2[i][j - 1] == 1 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 0 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 1) {
                tablero2[i][j] = 1;
            } else if (tablero2[i][j - 1] == 1 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 1 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 0) {
                tablero2[i][j] = 1;
            } else if (tablero2[i][j - 1] == 1 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 1 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 1) {
                tablero2[i][j] = 1;
            } else {
                tablero2[i][j] = 0;
            }

        }
    }
}
/*
combinacion que hace formar corazones lol
 if (tablero2[i][j - 1] == 1 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 0 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 0) {
                tablero2[i][j] = 1; //vivo  
            } else if (tablero2[i][j - 1] == 0 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 1 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 1) {
                tablero2[i][j] = 1;
            } else if (tablero2[i][j - 1] == 0 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 1 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 0) {
                tablero2[i][j] = 1;
            } else if (tablero2[i][j - 1] == 1 && tablero2[(i + 1 + columnas) % columnas][j - 1] == 1 && tablero2[(i + 2 + columnas) % columnas][j - 1] == 1) {
                tablero2[i][j] = 1;

 para esto me base en http://www.cs.us.es/~fsancho/?e=66
https://en.wikipedia.org/wiki/Cellular_automaton
interesante: https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/modeling-natural-systems/gameOfLife2.html
https://www.nathaniel.ai/majority-classification/
*/
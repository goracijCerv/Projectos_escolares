//Implementacion del juego de la vida
function tablero(col, fil) { //creando el tablero del juego
    let y = new Array(col);
    for (let i = 0; i < y.length; i++) {
        y[i] = new Array(fil);
    }
    return y
}
let columnas;
let filas;
let resolucion = 5; //ayuda a darle un tamaño a las celulas  
let tablero2;

function setup() { //inicando el juego
    createCanvas(1320, 620);
    columnas = width / resolucion;
    filas = height / resolucion;
    tablero2 = tablero(columnas, filas);
    for (let i = 0; i < columnas; i++) {
        for (let j = 0; j < filas; j++) {
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
    //calculando el sigueinte tablero 
    let sig = tablero(columnas, filas);
    for (let i = 0; i < columnas; i++) {
        for (let j = 0; j < filas; j++) {
            let estado = tablero2[i][j];
            //contamos a los vivos
            let sum = 0;
            let vecinos = contarVecinos(tablero2, i, j);
            if (estado == 0 && vecinos == 3) { //priemra regla si una celula esta muerta pero tiene 3 vecinos vivos revive
                sig[i][j] = 1;
            } else if (estado == 1 && (vecinos < 2 || vecinos > 3)) { //si esta viva pero tiene menos de 3 vecinos o mas de 3 se muere
                sig[i][j] = 0;
            } else {
                sig[i][j] = estado; //si no se cumple las condiciones no cambia
            }

        }
    }
    tablero2 = sig; // cambiamos de estado
}

function contarVecinos(tab, x, y) {
    let cont = 0;
    for (let i = -1; i < 2; i++) {
        for (let j = -1; j < 2; j++) { //contamos vecionos en forma de caballo
            let col = (x + i + columnas) % columnas;
            let row = (y + j + filas) % filas; //ayuda para evitar los bordes haciendo que de la vuelta hacia el otro lado
            cont += tab[col][row];
        }
    }
    cont -= tab[x][y] //en dado caso que nuestra posicion este viva la eliminamos del conteo de vecinos
    return cont;
}